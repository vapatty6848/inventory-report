from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if path.split('.')[1] != "csv":
            raise ValueError("Arquivo inválido")

        return CsvImporter.read_csv(path)

    def read_csv(path):
        productList = []
        with open(path) as file:
            fileContent = csv.DictReader(file)
            [productList.append(item) for item in fileContent]

        return productList
