from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        file_type = path.split(".")[-1]
        if file_type != "json":
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            content = file.read()  # leitura do arquivo
        data = json.loads(content)
        return data
