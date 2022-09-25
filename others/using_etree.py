import xml.etree.ElementTree as ET

# Parse xml from a filename
element_tree = ET.parse("xml_c.xml")

# alternatively, we can read the XML document
# incrementally with a streaming pull parser,
# which yields a sequence of events and elements


# which only emits end events associated with the closing XML tags
for event, element in ET.iterparse("xml_c.xml"):
    print(event, element)

# for getting the other events, we'll do this
for event, element in ET.iterparse("xml_c.xml", ["comment"]):
    print(element.text.strip())

"""
All other events are:
1. start: Start of an element
2. end: End of an element
3. comment: Comment element
4. pi: Processing instruction, as in XSL
5. start-ns: Start of a namespace
6. end-ns: End of a namespace
"""

for event, element in ET.iterparse("xml_c.xml", ['start', 'end']):
    print(element.text.strip())
