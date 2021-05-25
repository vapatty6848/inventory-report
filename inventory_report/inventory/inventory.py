from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    def __init__(self):
        self.a = "teste 123"

    def simple_complex(data_list, data_type):
        if (data_type == "simples"):
            return SimpleReport.generate(data_list)
        else:
            return CompleteReport.generate(data_list)

    def import_data(path, data_type):
        extension = path.split('.')[-1]
        with open(path, 'r') as file:
            if (extension == 'json'):
                read = file.read()
                json_list = json.loads(read)
                return Inventory.simple_complex(json_list, data_type)
            elif (extension == 'csv'):
                mycsv = csv.DictReader(file, delimiter=",")
                csv_list = []
                for row in mycsv:
                    csv_list.append(row)
                return Inventory.simple_complex(csv_list, data_type)
            elif (extension == 'xml'):
                doc = xmltodict.parse(file.read())
                xml_list = doc["dataset"]["record"]
                return Inventory.simple_complex(xml_list, data_type)
