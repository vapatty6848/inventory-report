from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(file):
        if file.endswith('.xml'):
            inventory_data = []
            with open(file) as xml_file:
                tree = ET.parse(xml_file)
                root = tree.getroot()
                all_records = root.findall('record')
                for item in all_records:
                    inventory = {element.tag: element.text for element in item}
                    inventory_data.append(inventory)
            return inventory_data
        else:
            raise ValueError("Arquivo inválido")
