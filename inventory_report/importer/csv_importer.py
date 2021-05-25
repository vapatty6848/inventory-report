from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith('.csv'):
            file = Inventory.open_csv_file(file_name)
            return file
        else:
            raise ValueError("Arquivo inválido")
