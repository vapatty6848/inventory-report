import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def _csvImporter(cls, file_path):
        content_list = []
        with open(file_path, newline='') as csvfile:
            content = csv.DictReader(csvfile, delimiter=",")
            for row in content:
                current = {}
                for key in row:
                    current[key] = row[key]
                content_list.append(current)

        return content_list

    @classmethod
    def _jsonImporter(cls, file_path):
        content_list = []
        with open(file_path, newline='') as jsonfile:
            content_list = json.load(jsonfile)

        return content_list

    @classmethod
    def _xmlImporter(cls, file_path):
        content_list = []
        with open(file_path, newline='') as xmlfile:
            content = csv.DictReader(xmlfile, delimiter=",")
            for row in content:
                current = {}
                for key in row:
                    current[key] = row[key]
                content_list.append(current)
        return content_list

    @classmethod
    def _call_importer(cls, file_path):
        extension = file_path.split('.')[-1]
        if extension == 'csv':
            return cls._csvImporter(file_path)
        elif extension == 'json':
            return cls._jsonImporter(file_path)
        elif extension == 'xml':
            return cls._xmlImporter(file_path)
        else:
            return None

    @classmethod
    def _generate_report(cls, content, report_type):
        if report_type == "simples":
            return SimpleReport.generate(content)
        elif report_type == "completo":
            return CompleteReport.generate(content)

    @classmethod
    def import_data(cls, file_path, report_type):
        content_list = cls._call_importer(file_path)
        return cls._generate_report(content_list, report_type)
