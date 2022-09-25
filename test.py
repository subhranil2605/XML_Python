import concurrent.futures
import time
import parsing
import requests


# Finished in 5.2739394000018365 seconds
# for link in links:
#     data_bytes = requests.get(link).content
#     file_name = link.split('/')[-1]
#     file_name = f"files/{file_name}"
#
#     with open(file_name, 'wb') as f:
#         f.write(data_bytes)
#         print(f"{file_name} downloaded...")


def download(link):
    data_bytes = requests.get(link).content
    file_name = link.split('/')[-1]
    file_name = f"files/{file_name}"

    with open(file_name, 'wb') as f:
        f.write(data_bytes)
        print(f"{file_name} downloaded...")


if __name__ == '__main__':
    rslt_docs = parsing.read_xml("xml_file.xml")
    docs_ = parsing.get_docs_by_file_type(rslt_docs, "DLTINS")
    links = [link[0] for link in parsing.get_download_links(docs_)]

    t1 = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download, links)

    t2 = time.perf_counter()

    print(f"Finished in {t2 - t1} seconds!!")
