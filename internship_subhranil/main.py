import os
from pathlib import Path
from parsing import read_xml, get_docs_by_file_type, get_download_links
from downloading import download
from extracting import extract
from create_csv_from_xml import convert
from uploading import create_bucket, upload
import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")

# to save in a log file
# logging.basicConfig(filename="test.log", level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")

if __name__ == '__main__':
    logging.info("Parsing Start!!!")
    # parsing download links from given XML file
    rslt_docs = read_xml("xml_file.xml")
    docs_ = get_docs_by_file_type(rslt_docs, "DLTINS")
    links = [link[0] for link in get_download_links(docs_)]
    logging.info(links)
    logging.info("Parsing Done!!!")

    logging.info("Downloading Start!!!")
    # downloading zip files from the parsed links
    download(links)
    logging.info("Downloading Done!!!")

    logging.info("Extracting Start!!!")
    # extracting downloaded zip files to get xml files
    path = os.path.join(os.getcwd(), 'files')
    zip_files = (file for file in Path(path).iterdir() if file.suffix == '.zip')
    extract(zip_files)
    logging.info("Extracting Done!!!")

    logging.info("Converting Start!!!")
    # converting xml files
    path = Path(os.path.join(os.getcwd(), "files/extracted_files"))
    xml_files = (file for file in Path(path).iterdir() if file.suffix == '.xml')
    convert(xml_files)
    logging.info("Converting Done!!!")

    logging.info("Upload to the AWS S3 bucket")
    path = Path(os.path.join(os.getcwd(), "files/extracted_csvs"))
    csv_files = (file for file in path.iterdir() if file.suffix == '.csv')  # all the csv files
    create_bucket()  # creating bucket
    [upload(csv_file) for csv_file in csv_files]  # upload each file
    logging.info("Uploading Done!!!")
