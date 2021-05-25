import csv
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, data_path, data_type):
        with open(data_path) as data:
            data_reader = csv.DictReader(data)
            array_data = [data for data in data_reader]
            return SimpleReport.generate(array_data)
