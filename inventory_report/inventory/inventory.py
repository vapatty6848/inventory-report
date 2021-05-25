import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


# https://docs.python.org/pt-br/3/library/csv.html
def open_csv_file(path):
    with open(path) as csv_file:
        file = csv.DictReader(csv_file)
        return list(file)


def open_json_file(path):
    with open(path) as json_file:
        file = json.load(json_file)
        return file


# https://raccoon.ninja/pt/dev-pt/manipulando-xml-com-python/
def open_xml_file(path):
    root = ET.parse(path).getroot()
    registers = root.findall("record")
    print(registers)
    file = [] 
    for register in registers:
        file_dict = {}
        for tag in register:
            file_dict[tag.tag] = tag.text
        file.append(file_dict)
    return file


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        if path.endswith('.csv'):
            data = open_csv_file(path)
        if path.endswith('.json'):
            data = open_json_file(path)
        if path.endswith('.xml'):
            data = open_xml_file(path)
        if report_type == "simples":
            report = SimpleReport.generate(data)
        else:
            report = CompleteReport.generate(data)
        return report
