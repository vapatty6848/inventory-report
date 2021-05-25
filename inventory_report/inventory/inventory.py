from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, csv_file, type):
        simple_report = SimpleReport
        complete_report = CompleteReport
        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile)
            csv_content = list(reader)
        if type == "simples":
            return simple_report.generate(csv_content)
        if type == "completo":
            return complete_report.generate(csv_content)


#     def __init__(self, csv_file, type):
#         self.csv_file = csv_file
#         self.type = type

#     def read_csv(self, csv_file):
#         with open(csv_file) as csvfile:
#             reader = csv.DictReader(csvfile)
#             return list(reader)

#     def import_data(self, csv_file, type):
#         csv_content = self.read_csv(Inventory, csv_file)
#         simple_report = SimpleReport
#         complete_report = CompleteReport
#         if type == "simples":
#             return simple_report.generate(csv_content)
#         if type == "completo":
#             return complete_report.generate(csv_content)
