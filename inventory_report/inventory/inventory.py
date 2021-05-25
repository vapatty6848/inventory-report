from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    def __init__(self, csv_file, type):
        self.csv_file = csv_file
        self.type = type

    # requisito 3
    @classmethod
    def read_csv(cls, csv_file):
        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)

    # requisito 4
    @classmethod
    def read_json(cls, json_file):
        with open(json_file) as jsonfile:
            reader = json.load(jsonfile)
            return list(reader)

    # requisito 5
    @classmethod
    def read_xml(cls, xml_file):
        with open(xml_file, 'r') as xmlfile:
            data_dict = xmltodict.parse(xmlfile.read())
            json_file = json.dumps(data_dict)
            return json.loads(json_file)['dataset']['record']

    @classmethod
    def import_data(cls, file, type):
        reader_map = {
            "csv": Inventory.read_csv,
            "json": Inventory.read_json,
            "xml": Inventory.read_xml
        }
        extension = file.split('.')[1]
        result = reader_map[extension](file)
        if type == "simples":
            return SimpleReport.generate(result)
        if type == "completo":
            return CompleteReport.generate(result)
