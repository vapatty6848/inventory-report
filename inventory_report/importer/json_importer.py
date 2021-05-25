from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if path.split('.')[1] != "json":
            raise ValueError("Arquivo inválido")

        return JsonImporter.read_json(path)

    def read_json(path):
        with open(path) as file:
            content = json.load(file)
            return content
