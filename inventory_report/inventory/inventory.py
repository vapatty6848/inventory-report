import csv
import json
import xml.etree.ElementTree as element_tree
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def read_csv(filepath):
    with open(filepath) as file:
        csv_data = csv.DictReader(file)
        return list(csv_data)


def read_json(filepath):
    with open(filepath) as file:
        return json.load(file)


def read_xml(file):
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
            new_report = read_csv(test)
        if test.endswith(".json"):
            new_report = read_json(test)
        if test.endswith(".xml"):
            new_report = read_xml(test)
        if type == "completo":
            new_report = CompleteReport.generate(new_report)
        else:
            new_report = SimpleReport.generate(new_report)
        return new_report