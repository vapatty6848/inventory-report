from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, caminho):
        if not caminho.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        return Importer.choose_reader(caminho)
