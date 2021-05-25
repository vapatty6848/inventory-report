from inventory_report.importer.importer import Impoter
import csv


class CsvImporter(Impoter):
    def __init__(self, path):
        self.path = path

    def data_import(self):
        listOfdicts = []
        with open(self.path, mode='r') as li:
            reader = csv.DictReader(li)
            for row in reader:
                listOfdicts.append(row)
        return listOfdicts
