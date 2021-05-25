import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
# https://docs.python.org/3/library/csv.html


class Inventory:
    @classmethod
    def import_data(cls, data_path, data_type):
        with open(data_path) as data:
            data_reader = csv.DictReader(data)
            array_data = [data for data in data_reader]
            if data_type == 'simples':
                return SimpleReport.generate(array_data)
            return CompleteReport.generate(array_data)