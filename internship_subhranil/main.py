import os
from pathlib import Path
from parsing import read_xml, get_docs_by_file_type, get_download_links
from downloading import download
from extracting import extract
from create_csv_from_xml import convert

if __name__ == '__main__':
    print("Parsing Start!!!")
    # parsing download links from given XML file
    rslt_docs = read_xml("xml_file.xml")
    docs_ = get_docs_by_file_type(rslt_docs, "DLTINS")
    links = [link[0] for link in get_download_links(docs_)]
    print(links)
    print("Parsing Done!!!")

    print("\nDownloading Start!!!")
    # downloading zip files from the parsed links
    download(links)
    print("Downloading Done!!!")

    print("\nExtracting Start!!!")
    # extracting downloaded zip files to get xml files
    path = os.path.join(os.getcwd(), 'files')
    zip_files = (file for file in Path(path).iterdir() if file.suffix == '.zip')
    extract(zip_files)
    print("Extracting Done!!!")

    print("\nConverting Start!!!")
    # converting xml files
    path = Path(os.path.join(os.getcwd(), "files/extracted_files"))
    xml_files = (file for file in Path(path).iterdir() if file.suffix == '.xml')
    convert(xml_files)
    print("Converting Done!!!")
