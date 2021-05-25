from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(url):
        if url.endswith('.csv'):
            with open(url) as file:
                csv_file = csv.DictReader(file)
                return list(csv_file)
        else:
            raise ValueError("Arquivo inválido")
