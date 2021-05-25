from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, caminho):
        if not caminho.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        return Importer.choose_reader(caminho)
