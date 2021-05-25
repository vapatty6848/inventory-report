from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if path.split(".", 1)[1] != "json":
            raise ValueError("Arquivo inválido")
        return JsonImporter.leitor_json(path)

    def leitor_json(path):
        with open(path) as file:
            content = json.load(file)
            return content
