from inventory_report.importer.importer import Importer
import csv


def read_csv(path):
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


class CsvImporter(Importer):
    @classmethod
    def import_data(self, file):
        is_csv = file.endswith(".csv")

        if not is_csv:
            raise ValueError("Arquivo inválido")

        preparedList = read_csv(file)
        return preparedList
