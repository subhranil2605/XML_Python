from xml.dom import minidom
from xml.dom.minidom import Document, Element
from xml.dom.minicompat import NodeList


def read_xml(filename: str):
    try:
        # Open the XML file
        dom_tree: Document = minidom.parse(filename)

        # root element
        root: Element = dom_tree.documentElement

        # Result
        result: Element = root.getElementsByTagName('result')[0]
        result_docs: NodeList = result.getElementsByTagName('doc')
        return result_docs
    except Exception as e:
        print(e)


def get_docs_by_file_type(result_docs: NodeList, file_type: str):
    docs_with_dltins = []
    for doc in result_docs:
        doc_strs = doc.getElementsByTagName('str')
        for s in doc_strs:
            if s.getAttribute("name") == "file_type":
                if s.childNodes[0].data == file_type:
                    docs_with_dltins.append(s.parentNode)
    return docs_with_dltins


def get_download_links(docs):
    return [[i.childNodes[0].data for i in doc.getElementsByTagName('str') if
             i.getAttribute("name") == "download_link"] for doc in docs]


if __name__ == '__main__':
    rslt_docs = read_xml("xml_c.xml")
    docs_ = get_docs_by_file_type(rslt_docs, "DLTINS")
    links = get_download_links(docs_)
    print(links)
