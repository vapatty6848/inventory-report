from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, caminho):
        if not caminho.endswith(".json"):
            raise ValueError("Arquivo inválido")
