import concurrent.futures
import time
import os
from pathlib import Path
import zipfile



def extract_zip(zip_file):
    path = os.path.join(os.getcwd(), 'files')
    target_path = Path(os.path.join(os.getcwd(), 'files/extracted_files'))
    zip_files = (file for file in Path(path).iterdir() if file.suffix == '.zip')
    
    if not target_path.is_dir():
        os.mkdir(target_path)
        
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(target_path)
        print(f"{zip_file} extracted...")


def extract(zip_files_):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract_zip, zip_files_)
