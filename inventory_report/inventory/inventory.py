import csv
import json
import xml.etree.ElementTree as ET
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
    def read_xml(cls, path):
        with open(path) as file:
            inventory_list = []
            xml_tree = ET.parse(file)
            root = xml_tree.getroot()
            for child in root.iter("record"):
                item = {}
                for record_child in child.iter("*"):
                    if record_child.tag != "record":
                        item[record_child.tag] = record_child.text
                inventory_list.append(item)
            return inventory_list

    @classmethod
    def import_data(cls, path, type):
        if path.endswith(".csv"):
            file_content = cls.read_csv(path)
        if path.endswith(".json"):
            file_content = cls.read_json(path)
        if path.endswith(".xml"):
            file_content = cls.read_xml(path)
        if type == "simples":
            file_content = SimpleReport.generate(file_content)
        else:
            file_content = CompleteReport.generate(file_content)
        return file_content
