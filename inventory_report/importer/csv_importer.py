import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path):
        Importer.validate_extension(file_path, "csv")

        with open(file_path) as csvfile:
            products = list(csv.DictReader(csvfile))

            return products
