from xml.dom import minidom
from xml.dom.minidom import Document, Element
from xml.dom.minicompat import NodeList

# Open the XML file
dom_tree: Document = minidom.parse("xml_c.xml")

response: Element = dom_tree.documentElement

children: NodeList = response.childNodes

"""
lst: Element = response.getElementsByTagName('lst')[0]
ints: NodeList = lst.getElementsByTagName('int')
for i in ints:
    for k, v in i.attributes.items():
        print(k, v, i.childNodes[0].data)

lst_2 = lst.getElementsByTagName('lst')[0]
strs = lst_2.getElementsByTagName('str')
for s in strs:
    for k, v in s.attributes.items():
        print(k, v, s.childNodes[0].data)

"""

# Result
result = response.getElementsByTagName('result')[0]

# attributes in result
# for key, value in result.attributes.items():
#     print(key, value)

result_docs = result.getElementsByTagName('doc')

for doc in result_docs:
    doc_strs = doc.getElementsByTagName('str')
    for s in doc_strs:
        if s.getAttribute("name") == "file_type":
            if s.childNodes[0].data == "DLTINS":
                [print(i.childNodes[0].data) for i in doc.getElementsByTagName('str') if
                 i.getAttribute("name") == "download_link"]

# def get_download_lins(docs):
#     for doc in result_docs:
#         doc_strs = doc.getElementsByTagName('str')
#         for s in doc_strs:
#             if s.getAttribute("name") == "file_type":
#                 if s.childNodes[0].data == "DLTINS":
#                     [print(i.childNodes[0].data) for i in s.parentNode.getElementsByTagName('str') if
#                      i.getAttribute("name") == "download_link"]
