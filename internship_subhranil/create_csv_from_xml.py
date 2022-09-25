import xml.etree.ElementTree as ET
import os
import csv
import codecs
from pathlib import Path
import concurrent.futures

path = Path(os.path.join(os.getcwd(), "files/extracted_files"))
target_path = Path(os.path.join(os.getcwd(), "files/extracted_csvs"))

xml_files = (file for file in Path(path).iterdir() if file.suffix == '.xml')


def get_tag_name(t: str):
    idx = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t


def creating_csv(xml_file):
    csv_filename = xml_file.name.replace(".xml", ".csv")
    target = os.path.join(target_path, csv_filename)

    print(f"Converting {csv_filename} started!!!")
    with codecs.open(target, "w", "utf-8") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([
            'FinInstrmGnlAttrbts.Id', 'FinInstrmGnlAttrbts.FullNm', 'FinInstrmGnlAttrbts.ClssfctnTp',
            'FinInstrmGnlAttrbts.CmmdtyDerivInd', 'FinInstrmGnlAttrbts.NtnlCcy', 'Issr'
        ])

        for event, elem in ET.iterparse(xml_file, events=("start", "end")):
            t_name = get_tag_name(elem.tag)

            if event == 'start':
                if t_name == 'TermntdRcrd':
                    for t in elem:
                        if get_tag_name(t.tag) == 'FinInstrmGnlAttrbts':
                            for a in t:
                                if get_tag_name(a.tag) == 'Id':
                                    id_ = a.text
                                elif get_tag_name(a.tag) == 'FullNm':
                                    full_name = a.text
                                elif get_tag_name(a.tag) == 'ClssfctnTp':
                                    cft = a.text
                                elif get_tag_name(a.tag) == 'CmmdtyDerivInd':
                                    cdi = a.text
                                elif get_tag_name(a.tag) == 'NtnlCcy':
                                    nc = a.text

                        elif get_tag_name(t.tag) == 'Issr':
                            issr = t.text

                    csv_writer.writerow([id_, full_name, cft, cdi, nc, issr])

                elif t_name == 'ModfdRcrd':
                    for t in elem:
                        if get_tag_name(t.tag) == 'FinInstrmGnlAttrbts':
                            for a in t:
                                if get_tag_name(a.tag) == 'Id':
                                    id_ = a.text
                                elif get_tag_name(a.tag) == 'FullNm':
                                    full_name = a.text
                                elif get_tag_name(a.tag) == 'ClssfctnTp':
                                    cft = a.text
                                elif get_tag_name(a.tag) == 'CmmdtyDerivInd':
                                    cdi = a.text
                                elif get_tag_name(a.tag) == 'NtnlCcy':
                                    nc = a.text

                        elif get_tag_name(t.tag) == 'Issr':
                            issr = t.text

                    csv_writer.writerow([id_, full_name, cft, cdi, nc, issr])

            elem.clear()

        print(f"{target} Done")


def convert(xml_files_):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(creating_csv, xml_files_)
