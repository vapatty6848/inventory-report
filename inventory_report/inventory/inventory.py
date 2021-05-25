import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def read_csv(cls, path):
        with open(path) as file:
            csv_file = csv.DictReader(file)
            return list(csv_file)

    @classmethod
    def import_data(cls, path, type):
        file_content = ""
        if path.endswith(".csv"):
            file_content = cls.read_csv(path)
        if type == "simples":
            file_content = SimpleReport.generate(file_content)
        else:
            file_content = CompleteReport.generate(file_content)
        return file_content
