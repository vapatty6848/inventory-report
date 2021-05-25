import json

from inventory_report.importer.importer import Importer

class JsonImporter(Importer):
    @staticmethod
    def import_data(file_path):
        Importer.validate_extension(file_path, 'json')

        with open(file_path) as jsonFile:
            products = list(json.load(jsonFile))

            return products
