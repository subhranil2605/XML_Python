import concurrent.futures
import os
from pathlib import Path
import zipfile
import logging
from typing import Sequence, Generator

# configuring logging
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")


# logging.basicConfig(filename="test.log", level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")


def extract_zip(zip_file: str) -> None:
    """
    Extract a zip file
    :param zip_file: a zip filename
    :return: None
    """

    # target directory
    target_path = Path(os.path.join(os.getcwd(), 'files/extracted_files'))

    if not target_path.is_dir():
        logging.debug(f"target folder doesn't exist so created.")
        os.mkdir(target_path)  # creating directory

    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(target_path)  # extract all the files in the zip
            logging.info(f"{zip_file} extracted...")
    except FileNotFoundError:
        logging.critical(f"File not found: {zip_file}")
        raise FileNotFoundError


def extract(zip_files_: Generator | Sequence) -> None:
    """
    concurrenty extract all the zip files given in a sequence or generator object
    :param zip_files_: Generator object or Sequence
    :return: None
    """

    # using threading to save multiple files
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract_zip, zip_files_)
