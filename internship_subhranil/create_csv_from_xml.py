import xml.etree.ElementTree as ET
import os
import csv
import codecs
from pathlib import Path
import concurrent.futures
import logging
from typing import Generator, Sequence

# configuring logging
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")


# logging.basicConfig(filename="test.log", level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")

def get_tag_name(t: str):
    """
    Extracting tag name from a string
    :param t: a string
    :return: tag name
    """
    idx = t.rfind("}")  # find for a right curly braces
    if idx != -1:  # if not index is not last
        t = t[idx + 1:]  # tag name
    return t


def creating_csv(xml_file):
    target_path = Path(os.path.join(os.getcwd(), "files/extracted_csvs"))

    # if target directory does not exist
    if not target_path.is_dir():
        logging.debug(f"target folder doesn't exist so created.")
        os.mkdir(target_path)

    csv_filename = xml_file.name.replace(".xml", ".csv")  # csv filename
    target = os.path.join(target_path, csv_filename)  # where to save csv

    logging.info(f"Converting {csv_filename} started!!!")

    with codecs.open(target, "w", "utf-8") as f:

        # csv writer instance
        csv_writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

        # write the column
        csv_writer.writerow([
            'FinInstrmGnlAttrbts.Id', 'FinInstrmGnlAttrbts.FullNm', 'FinInstrmGnlAttrbts.ClssfctnTp',
            'FinInstrmGnlAttrbts.CmmdtyDerivInd', 'FinInstrmGnlAttrbts.NtnlCcy', 'Issr'
        ])

        # traversing the document tree with iterparse to save memory
        for event, elem in ET.iterparse(xml_file, events=("start", "end")):
            t_name = get_tag_name(elem.tag)  # tag name

            # if the event is start
            if event == 'start':

                # if the tag name is 'TermntdRcrd':
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

                    # save the data in csv file
                    csv_writer.writerow([id_, full_name, cft, cdi, nc, issr])

                # if the tag name is 'ModfdRcrd':
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

                    # save the data in csv file
                    csv_writer.writerow([id_, full_name, cft, cdi, nc, issr])

            elem.clear()

        logging.info(f"{target} Done")


def convert(xml_files_: Generator | Sequence) -> None:
    """
    concurrenty convert all the XML files into CSV with given data
    :param xml_files_: xml files
    :return: None
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(creating_csv, xml_files_)
