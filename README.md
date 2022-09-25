# Working with XML files in python


## These things have been used

- Parsing with ```from xml.dom import minidom``` to get the ```download_links```
- Then Downloading from the links concurrently using ```concurrent.futures```
- After downloading the zip files, extract them using ```zipfile``` module and concurrency also used here.
- After extracting XML files from the zip files, first parse them using ```import xml.etree.ElementTree as ET```. Then create CSV files concurrently.