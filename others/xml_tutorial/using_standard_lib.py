from xml.dom.minidom import parse, parseString, Node
from xml.dom.minidom import Document, Element

# Parse XML from a filename
document: Document = parse("test.xml")

# XML declaration
print(document.version, document.encoding, document.standalone)

# Document type definition
dtd = document.doctype
print(dtd.entities["custom_entity"].childNodes)

# Document Root
root: Element = document.documentElement
print(root)

# Finding element by ID
# The sample SVG image has two nodes with an id attribute,
# but you can’t find either of them:
print(document.getElementById("skin"))
print(document.getElementById("smiley"))

# visit all elements recursively in Python
# check whether they have the id attribute
# and indicate it as their ID in one go:

print(root.getElementsByTagName("ellipse"))

# elements like <inkscape:custom> that are prefixed
# with a namespace identifier won’t be included.
# They must be searched using .getElementsByTagNameNS(),
# which expects different arguments

print(root.getElementsByTagNameNS(
    "http://www.inkscape.org/namespaces/inkscape",
    "custom"
))

element = root.getElementsByTagName("g")

# print(element)
# print(element[0].parentNode)
# print(element[0].firstChild)
# print(element[0].lastChild)
# print(element[0].nextSibling)
# print(element[0].previousSibling)

element_ = root.getElementsByTagName("g")[0]

print(f"Prefix: {element_.prefix}")
print(f"Tag Name: {element_.tagName}")
print(f"Attributes: {dict(element_.attributes.items())}")



