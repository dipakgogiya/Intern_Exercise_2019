#https://www.guru99.com/manipulating-xml-with-python.html
"""
To parse XML document
=> Import xml.dom.minidom
Use the function "parse" to parse the document ( doc=xml.dom.minidom.parse (file name);
Call the list of XML tags from the XML document using code (=doc.getElementsByTagName( "name of xml tags")

=> To create and add new attribute in XML document
Use function "createElement"

import xml.dom.minidom as minidom
#Use the parse() function to load and parse the xml file
xml_get_root = minidom.parse("account.xml") #Type is Instance

# print the nodename and child tagname from the file
print xml_get_root.nodeName # nodeName is the standard property name
print xml_get_root.firstChild.tagName # firstChild.tagName is also the standard property name

get_xml_data = xml_get_root.getElementsByTagName("template")

for xml_detail in get_xml_data:
    print xml_detail.getAttribute("id")

"""

import os 
from xml.etree import ElementTree

file_name = "account.xml"
file_path = os.path.abspath(os.path.join('./',file_name))

dom = ElementTree.parse(file_path)
course = dom.findall('template/xpath')
for c in course:
    print c.attrib
    
    
    
