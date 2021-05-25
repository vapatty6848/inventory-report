from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


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
    def read_json(cls, json_file):
        with open(json_file) as jsonfile:
            reader = json.load(jsonfile)
            return list(reader)

    @classmethod
    def read_xml(cls, xml_file):
        with open(xml_file, 'r') as xmlfile:
            data_dict = xmltodict.parse(xmlfile.read())
            json_file = json.dumps(data_dict)
            return json.loads(json_file)['dataset']['record']

    @classmethod
    def import_data(cls, file, type):
        simple_report = SimpleReport
        complete_report = CompleteReport
        if file.endswith(".csv"):
            result = Inventory.read_csv(file)
            if type == "simples":
                return simple_report.generate(result)
            if type == "completo":
                return complete_report.generate(result)
        if file.endswith(".json"):
            result = Inventory.read_json(file)
            if type == "simples":
                return simple_report.generate(result)
            if type == "completo":
                return complete_report.generate(result)
        if file.endswith(".xml"):
            result = Inventory.read_xml(file)
            if type == "simples":
                return simple_report.generate(result)
            if type == "completo":
                return complete_report.generate(result)


print(Inventory.read_xml('inventory_report/data/inventory.xml'))
