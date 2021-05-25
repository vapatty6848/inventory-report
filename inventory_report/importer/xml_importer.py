from inventory_report.importer.importer import Importer
from xml_to_dict import XMLtoDict


class XmlImporter(Importer):
    def import_data(path):
        if path.split(".", 1)[1] != "xml":
            raise ValueError("Arquivo inválido")
        return XmlImporter.leitor_xml(path)

    def leitor_xml(path):
        with open(path) as file:
            parser = XMLtoDict()
            xml_file = file.read()
            content = parser.value_from_nest("record", xml_file)
            return content
