import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

# https://docs.python.org/3/library/csv.html
# https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html


class Inventory:
    @staticmethod
    def import_data(data_path, data_type):
        data_path_end = data_path.split(".")[1]
        if data_path_end == "csv":
            return Inventory._csv_Import_Data(data_path, data_type)
        if data_path_end == "json":
            return Inventory._json_Import_Data(data_path, data_type)
        if data_path_end == "xml":
            return Inventory._xml_Import_Data(data_path, data_type)

    @staticmethod
    def _csv_Import_Data(data_path, data_type):
        with open(data_path) as data:
            data_reader = csv.DictReader(data)
            array_data = [data for data in data_reader]
            if data_type == "simples":
                return SimpleReport.generate(array_data)
            return CompleteReport.generate(array_data)

    @staticmethod
    def _json_Import_Data(data_path, data_type):
        with open(data_path) as data:
            array_data = json.load(data)
            if data_type == "simples":
                return SimpleReport.generate(array_data)
            return CompleteReport.generate(array_data)

    @staticmethod
    def _xml_Import_Data(data_path, data_type):
        with open(data_path) as data:
            array_data = xmltodict.parse(data.read())["dataset"]["record"]
            if data_type == "simples":
                return SimpleReport.generate(array_data)
            return CompleteReport.generate(array_data)


'''
class Inventory:
    @staticmethod
    def import_data(data_path, data_type):
        data_path_end = data_path.split(".")[1]
        if data_path_end == "csv":
            with open(data_path) as data:
                data_reader = csv.DictReader(data)
                array_data = [data for data in data_reader]
                if data_type == "simples":
                    return SimpleReport.generate(array_data)
                return CompleteReport.generate(array_data)
        elif data_path_end == "json":
            with open(data_path) as data:
                array_data = json.load(data)
                if data_type == "simples":
                    return SimpleReport.generate(array_data)
                return CompleteReport.generate(array_data)
        with open(data_path) as data:
            array_data = xmltodict.parse(data.read())["dataset"]["record"]
            if data_type == "simples":
                return SimpleReport.generate(array_data)
            return CompleteReport.generate(array_data)
'''
