import requests
import concurrent.futures
import os
from pathlib import Path
import logging

# configuring logging
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")


# logging.basicConfig(filename="test.log", level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")


def download_file(link: str) -> None:
    """
    download a single file and save in files folder.
    If the files directory not exists, then it creates and store
    downloaded files one by one concurrently

    :param link: url for the download link
    :return: None
    """

    target_path = Path(os.path.join(os.getcwd(), "files"))  # target directory

    try:
        response = requests.get(link)  # response

        # downloading the data using requests and store it in bytes
        data_bytes = response.content
    except requests.exceptions.ConnectionError:  # internet connection error
        logging.critical(f"Check your Internet Connection or URL!!!")
        raise ConnectionError
    except requests.exceptions.MissingSchema:
        logging.critical(f"Check your URL!!!")
        raise ValueError
    else:
        # file name is generated using link's last word
        file_name = os.path.join(target_path, link.split('/')[-1])

        # checks if the folder in the current dir exists
        if not target_path.is_dir():
            logging.debug(f"target folder doesn't exist so created.")
            os.mkdir(target_path)  # create the directory

        # writing the downloaded bytes in a file on local disk
        with open(file_name, 'wb') as f:
            f.write(data_bytes)
            logging.info(f"{file_name} downloaded...")


def download(links_: list) -> None:
    """
    concurrently download all the links given as a list
    :param links_: list of links
    :return: None
    """

    # using Threading for writing to the local disk
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_file, links_)
