import requests
import concurrent.futures
import parsing


def download_file(link):
    data_bytes = requests.get(link).content
    file_name = link.split('/')[-1]
    file_name = f'files/{file_name}'

    with open(file_name, 'wb') as f:
        f.write(data_bytes)
        print(f"{file_name} downloaded...")


def download(links_):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_file, links_)
