from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    # overriding abstract method
    @classmethod
    def import_data(cls, file):
        if file.split('.')[1] == 'json':
            return Inventory.read_json(file)
        else:
            raise ValueError("Arquivo inválido")
