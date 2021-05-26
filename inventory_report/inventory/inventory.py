from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from xml_to_dict import XMLtoDict
import csv
import json


class Inventory:
    def __init__(self):
        print("Inventory Report criado")

    @classmethod
    def extract_from_CSV(cls, file_path):
        with open(file_path) as file:
            csv_reader = csv.DictReader(file, delimiter=",")
            products = [row for row in csv_reader]
        return products

    @classmethod
    def extract_from_JSON(cls, file_path):
        with open(file_path) as file:
            products = json.load(file)
        return products

    @classmethod
    def extract_from_XML(cls, file_path):
        with open(file_path) as file:
            parser = XMLtoDict()
            xml_string = file.read()
            container_tag = "record"
            products = parser.value_from_nest(container_tag, xml_string)
        return products

    @classmethod
    def import_info(cls, file_path):
        if file_path.endswith(".csv"):
            products = cls.extract_from_CSV(file_path)

        if file_path.endswith(".json"):
            products = cls.extract_from_JSON(file_path)

        if file_path.endswith(".xml"):
            products = cls.extract_from_XML(file_path)

        return products

    @classmethod
    def import_data(cls, file_path, report_type):
        products = cls.import_info(file_path)

        if report_type == "simples":
            return SimpleReport.generate(products)

        if report_type == "completo":
            return CompleteReport.generate(products)
