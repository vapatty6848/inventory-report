from inventory_report.importer.importer import Importer
from inventory_report.utils.parse_xml import parse_xml


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path):
        Importer.validate_extension(file_path, "xml")

        with open(file_path) as xmlFile:
            products = list(parse_xml(xmlFile))

            return products
