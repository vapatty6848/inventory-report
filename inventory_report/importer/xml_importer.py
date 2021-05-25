from .importer import Importer
from inventory_report.inventory.inventory import read_xml


class XmlImporter(Importer):
    @classmethod
    def import_data(self, caminho):
        if not caminho.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        return read_xml(caminho)
