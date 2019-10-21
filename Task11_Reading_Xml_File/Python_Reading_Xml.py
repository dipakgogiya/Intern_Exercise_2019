#https://www.datacamp.com/community/tutorials/python-xml-elementtree

import xml.etree.ElementTree as ET

xml_data = ET.parse('account.xml')
xml_root = xml_data.getroot()

print ("Enter 'template' to show templates")
print ("Enter 'xpath' to show xpath")
print ("Enter 'link' to show link")
print ("Enter 'script' to show script")

get_input = raw_input("Enter Name you want to get :- ")
if get_input == 'template':
    for xmlpath in xml_root.findall('./'+get_input):
        print xmlpath.attrib
elif get_input == 'xpath':
    for xmlpath in xml_root.findall('./template/' + get_input):
        print xmlpath.attrib
elif get_input == 'link':
    for xmlpath in xml_root.findall('./template/xpath/' + get_input):
        print xmlpath.attrib
elif get_input == 'script':
    for xmlpath in xml_root.findall('./template/xpath/' + get_input):
        print xmlpath.attrib
else:
    print "Enter Valid Choice..."

for xmlpath in xml_root.findall("./template/[@id='_assets_backend_helpers']//"): #// Help To find all the content inside perticular id
    print "Id:",xmlpath.attrib
list = []   
for xmlpath in xml_root.findall("./template/xpath/script/[@src]"): #// Help To find all the content inside perticular id
    print "href = ",xmlpath.attrib['src']
    list.append(xmlpath.attrib['src'])
print list
