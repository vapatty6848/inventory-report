from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(file_path) as file:
            csv_reader = csv.DictReader(file, delimiter=",")
            products = [row for row in csv_reader]
        return products
