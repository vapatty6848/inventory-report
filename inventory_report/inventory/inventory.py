import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report):

        if path.endswith(".csv"):
            data = Inventory.csv_open(path)
        if path.endswith(".json"):
            data = Inventory.json_open(path)
        if path.endswith('xml'):
            data = Inventory.xml_open(path)

        if report == 'simples':
            return SimpleReport.generate(data)
        else:
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

    @staticmethod
    def xml_open(filepath):
        with open(filepath) as file:
            xml_dic = xmltodict.parse(file.read())
            xml_json = json.dumps(xml_dic)
            return json.loads(xml_json)['dataset']['record']
