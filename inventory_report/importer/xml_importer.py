from lxml import etree
from abc import abstractmethod
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @abstractmethod
    def import_data(file_path):
        extension = file_path.split('.')[-1]
        if extension != 'xml':
            raise ValueError('Arquivo inválido')

        content_list = []
        with open(file_path, newline='') as xmlfile:
            content = etree.parse(xmlfile)
            root = content.getroot()
            for child in root:
                current = {}
                for elem in child:
                    current[elem.tag] = elem.text

                content_list.append(current)
        return content_list
