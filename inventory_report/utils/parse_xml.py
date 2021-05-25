import xml.etree.ElementTree as ET

def parse_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()

    records = root.findall('record')

    items = []

    for record in records:
        item_dict = {}

        for node in record.iter():
            if (node.tag != 'record'):
                item_dict[node.tag] = node.text

        items.append(item_dict)

    return items
