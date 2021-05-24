import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):

        with open(path) as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)

            if report_type == 'simples':
                return SimpleReport.generate(data)

            if report_type == 'completo':
                return CompleteReport.generate(data)

