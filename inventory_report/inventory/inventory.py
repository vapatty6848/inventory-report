import csv
import json
import xml.etree.ElementTree as element_tree
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def read_data_csv(filepath):
    with open(filepath) as file:
        csv_data = csv.DictReader(file)
        return list(csv_data)


def read_data_json(filepath):
    with open(filepath) as file:
        return json.load(file)


def read_data_xml(file):
    root = element_tree.parse(file).getroot()
    data_tree = []
    for record in root:
        dict_format = {}
        for tag in record:
            dict_format[tag.tag] = tag.text
        data_tree.append(dict_format)
    return data_tree


class Inventory:
    @classmethod
    def import_data(self, test, type):
        if test.endswith(".csv"):
            data = read_data_csv(test)
        if test.endswith(".json"):
            data = read_data_json(test)
        if test.endswith(".xml"):
            data = read_data_xml(test)
        if type == "completo":
            new_report = CompleteReport.generate(data)
        else:
            new_report = SimpleReport.generate(data)
        return new_report