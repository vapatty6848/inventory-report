from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith('.xml'):
            file = Inventory.open_xml_file(file_name)
            return file
        else:
            raise ValueError("Arquivo inválido")
