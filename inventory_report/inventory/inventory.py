import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __init__(self):
        self.listOfdicts = []
        self.simpleReport = SimpleReport()
        self.completeReport = CompleteReport()

    def import_data(self, path='/home/danielmjales/Desktop/trybe/projects/sd-06-inventory-report/inventory_report/data/inventory.csv', reportType=''):
        with open(path, mode='r') as li:
            reader = csv.DictReader(li)
            for row in reader:
                self.listOfdicts.append(row)
        if reportType == 'simples':
            self.simpleReport.generate(self.listOfdicts)
        else:
            self.completeReport.generate(self.listOfdicts)
