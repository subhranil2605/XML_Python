from xml.dom import minidom
from xml.dom.minidom import Document, Element
from xml.dom.minicompat import NodeList
import logging

# configuring logging
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")


def read_xml(filename: str) -> NodeList | None:
    """
    Read XML file from the disk

    :param filename: filename of the xml file
    :return: NodeList
    """
    try:
        # open the XML file and create Document instance
        dom_tree: Document = minidom.parse(filename)
    except FileNotFoundError:
        logging.warning(f"{filename} is not valid!!!")
        raise FileNotFoundError
    else:
        logging.info(f"DOM Tree has been created {dom_tree}")

        # root element from the document tree
        root: Element = dom_tree.documentElement
        logging.info(f"The root element is {root}")

        # result tag from the xml file
        result: Element = root.getElementsByTagName('result')[0]
        logging.info(f"Parsed {result} from {root}")

        # all the doc elements as NodeList
        result_docs: NodeList = result.getElementsByTagName('doc')
        logging.info(f"Parsed list of {result_docs[0]} elements from {root}")

        return result_docs


def get_docs_by_file_type(result_docs: NodeList, file_type: str) -> list:
    """
    Get all the docs with provided file type

    :param result_docs: NodeList of the doc tag
    :param file_type: what type of file we're finding.
    :return: list
    :raise: AttributeError if valid nodelist not provided
    """

    assert len(result_docs) != 0, logging.warning("Nodelist is empty")

    # to store the docs with file_type DLTINS
    docs_with_dltins = list()

    for doc in result_docs:
        try:
            # elements with 'str' tag
            doc_strs: NodeList = doc.getElementsByTagName('str')
        except AttributeError:
            logging.warning("Invalid docs list provided")
            raise AttributeError
        else:
            for s in doc_strs:
                # if the attribute is file_type
                if s.getAttribute("name") == "file_type":
                    if s.childNodes[0].data == file_type:  # file_type is DLTINS
                        docs_with_dltins.append(s.parentNode)

    if docs_with_dltins:
        logging.info(f"Parsed all the doc element with file_type={file_type}")
    else:
        logging.warning(f"Could not parse any doc element list with file_type={file_type}")

    return docs_with_dltins


def get_download_links(docs: list) -> list:
    """
    Getting download links from the doc element
    :param docs: list of docs
    :return: list of download links
    """

    assert len(docs) != 0, logging.warning("Empty list")

    download_links: list = [[i.childNodes[0].data for i in doc.getElementsByTagName('str') if
                             i.getAttribute("name") == "download_link"] for doc in docs]

    logging.info("Parsed list of download links")
    logging.debug([link[0] for link in download_links])

    return download_links
