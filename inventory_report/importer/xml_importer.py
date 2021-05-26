from inventory_report.importer.importer import Importer
from xml_to_dict import XMLtoDict


class XmlImporter(Importer):
    def import_data(file_path):
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(file_path) as file:
            parser = XMLtoDict()
            xml_string = file.read()
            container_tag = "record"
            products = parser.value_from_nest(container_tag, xml_string)
        return products
