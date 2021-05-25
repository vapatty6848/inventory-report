from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    # overriding abstract method
    @classmethod
    def import_data(cls, file):
        if file.split('.')[1] == 'csv':
            return Inventory.read_csv(file)
        else:
            raise ValueError('Arquivo inválido')
