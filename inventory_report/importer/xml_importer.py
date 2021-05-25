from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(url):
        if url.endswith('.xml'):
            with open(url) as file:
                inventory_list = []
                xml_tree = ET.parse(file)
                root = xml_tree.getroot()
                for child in root.iter("record"):
                    item = {}
                    for record_child in child.iter('*'):
                        if record_child.tag != 'record':
                            item[record_child.tag] = record_child.text
                    inventory_list.append(item)
                return inventory_list
        else:
            raise ValueError("Arquivo inválido")
