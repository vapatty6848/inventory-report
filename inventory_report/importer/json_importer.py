from .importer import Importer
from inventory_report.inventory.inventory import read_json


class JsonImporter(Importer):
    @classmethod
    def import_data(self, caminho):
        if not caminho.endswith(".json"):
            raise ValueError("Arquivo inválido")
        return read_json(caminho)
