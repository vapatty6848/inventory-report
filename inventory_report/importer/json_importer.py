from inventory_report.importer.importer import Impoter
import json


class JsonImporter(Impoter):
    def __init__(self, path):
        self.path = path

    def data_import(self):
        listOfdicts = []
        with open(self.path) as f:
            listOfdicts = json.load(f)
        return listOfdicts
