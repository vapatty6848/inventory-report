from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith('.json'):
            file = Inventory.open_json_file(file_name)
            return file
        else:
            raise ValueError("Arquivo inválido")
