import concurrent.futures
import time
import os
from pathlib import Path
import zipfile

path = os.path.join(os.getcwd(), 'files')
target_path = os.path.join(os.getcwd(), 'files/extracted_files')
zip_files = (file for file in Path(path).iterdir() if file.suffix == '.zip')


def extract_zip(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(target_path)
        print(f"{zip_file} extracted...")


def extract(zip_files_):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract_zip, zip_files_)
