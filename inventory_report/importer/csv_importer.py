from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith('.csv'):
            inventory_data = []
            with open(path) as csv_file:
                inventory_data_csv = csv.DictReader(csv_file)
                [inventory_data.append(row) for row in inventory_data_csv]
            return inventory_data
        else:
            raise ValueError("Arquivo inválido")


result = CsvImporter()
print(result.import_data('inventory_report/data/inventory.csv'))
