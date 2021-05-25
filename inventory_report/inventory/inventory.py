import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(self, pathfile, type_report):
        with open(pathfile) as file:
            reporter_csv = csv.DictReader(file)
            reporter = []
            for row in reporter_csv:
                reporter.append(row)

            if type_report == 'simples':
                return SimpleReport.generate(reporter)
            else:
                return CompleteReport.generate(reporter)
