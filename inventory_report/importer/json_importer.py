from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(url):
        if url.endswith('.json'):
            with open(url) as file:
                json_file = json.load(file)
                return json_file
        else:
            raise ValueError("Arquivo inválido")
