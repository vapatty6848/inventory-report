from .importer import Importer
from inventory_report.inventory.inventory import read_csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, caminho):
        if not caminho.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        return read_csv(caminho)
