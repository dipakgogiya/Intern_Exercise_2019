import xml.etree.cElementTree as ET

xml_data = ET.ElementTree(file = 'account.xml')
xml_root = xml_data.getroot()
attribute_name = raw_input("Enter If you get link Enter 'link' or else Enter 'src' :- ")
for xml_child_tags in xml_root:
    print xml_child_tags.get('id')
    for xmlpath in xml_child_tags:
        print xmlpath.get('position')
        for attr in xmlpath:
            if attr.tag == attribute_name:
                print attr.get('href')
            elif attr.tag == attribute_name:
                print attr.get('src')