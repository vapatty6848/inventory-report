from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
from xml_to_dict import XMLtoDict


class Inventory:
    def import_data(path, type):
        if path.split('.')[1] == "csv":
            report = Inventory.read_csv(path)

        if path.split('.')[1] == "json":
            report = Inventory.read_json(path)

        if path.split('.')[1] == "xml":
            report = Inventory.read_xml(path)

        if type == "simples":
            return SimpleReport.generate(report)
        else:
            return CompleteReport.generate(report)

    def read_csv(path):
        productList = []
        with open(path) as file:
            fileContent = csv.DictReader(file)
            [productList.append(item) for item in fileContent]

        return productList

    def read_json(path):
        with open(path) as file:
            content = json.load(file)
            return content

    def read_xml(path):
        with open(path) as file:
            parser = XMLtoDict()
            xml_file = file.read()
            content = parser.value_from_nest("record", xml_file)
            return content
