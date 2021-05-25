from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        extension = path.split('.')[-1]
        if (extension != 'xml'):
            raise ValueError('Arquivo inválido')
        with open(path, 'r') as file:
            doc = xmltodict.parse(file.read())
            xml_list = doc["dataset"]["record"]
        return xml_list
