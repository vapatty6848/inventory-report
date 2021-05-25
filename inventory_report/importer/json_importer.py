from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(file):
        if file.endswith('.json'):
            with open(file) as json_file:
                inventory_data_json = json.load(json_file)
            return inventory_data_json
        else:
            raise ValueError("Arquivo inválido")


result = JsonImporter()
print(result.import_data('inventory_report/data/inventory.json'))
