from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if path.split(".", 1)[1] != "csv":
            raise ValueError("Arquivo inválido")
        return CsvImporter.leitor_csv(path)

    def leitor_csv(path):
        lista_produtos = []
        with open(path, newline="") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                lista_produtos.append(row)
        return lista_produtos
