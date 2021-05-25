import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report):

        if path.endswith(".csv"):
            data = Inventory.csv_open(path)
        if path.endswith(".json"):
            data = Inventory.json_open(path)

        if report == 'simples':
            return SimpleReport.generate(data)

        if report == 'completo':
            return CompleteReport.generate(data)

    @staticmethod
    def csv_open(filepath):
        with open(filepath) as file:
            data = csv.DictReader(file)
            return list(data)

    @staticmethod
    def json_open(filepath):
        with open(filepath) as file:
            return json.load(file)
