from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import json
import csv
import xmltodict


class Inventory:
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
            data = xmltodict.parse(xmlfile.read())
            json = json.dumps(data)
            return json.loads(json)['dataset']['record']

    @classmethod
    def import_data(cls, file, type):
        reader = {
          "csv": Inventory.read_csv,
          "json": Inventory.read_json,
          "xml": Inventory.read_xml
        }
        extension = file.split('.')[1]
        res = reader[extension](file)
        if type == "simples":
            return SimpleReport.generate(res)
        if type == "completo":
            return CompleteReport.generate(res)
