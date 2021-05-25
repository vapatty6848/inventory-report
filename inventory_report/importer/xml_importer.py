from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    # overriding abstract method
    @classmethod
    def import_data(cls, file):
        if file.split('.')[1] == 'xml':
            return Inventory.read_xml(file)
        else:
            raise ValueError("Arquivo inválido")
