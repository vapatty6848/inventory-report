import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def read_csv(cls, path):
        with open(path) as file:
            csv_file = csv.DictReader(file)
            return list(csv_file)

    @classmethod
    def read_json(cls, path):
        with open(path) as file:
            json_file = json.load(file)
            return json_file

    @classmethod
    def import_data(cls, path, type):
        file_content = ""
        if path.endswith(".csv"):
            file_content = cls.read_csv(path)
        if path.endswith(".json"):
            file_content = cls.read_json(path)
        if type == "simples":
            file_content = SimpleReport.generate(file_content)
        elif type == "completo":
            file_content = CompleteReport.generate(file_content)
        return file_content
