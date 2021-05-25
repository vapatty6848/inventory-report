from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    def __init__(self, csv_file, type):
        self.csv_file = csv_file
        self.type = type

    @classmethod
    def read_csv(cls, csv_file):
        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)

    @classmethod
    def import_data(cls, csv_file, type):
        csv_content = cls.read_csv(csv_file)
        simple_report = SimpleReport
        complete_report = CompleteReport
        if type == "simples":
            return simple_report.generate(csv_content)
        if type == "completo":
            return complete_report.generate(csv_content)
