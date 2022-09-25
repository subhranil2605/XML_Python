import requests
import concurrent.futures
import os
from pathlib import Path


def download_file(link):
    target_path = Path(os.path.join(os.getcwd(), "files"))
    if not target_path.is_dir():
        os.mkdir(target_path)

    data_bytes = requests.get(link).content
    file_name = os.path.join(target_path, link.split('/')[-1])

    with open(file_name, 'wb') as f:
        f.write(data_bytes)
        print(f"{file_name} downloaded...")


def download(links_):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_file, links_)
