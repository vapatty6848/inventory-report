import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        file_extension = file_path.split(".")[1]
        if file_extension == "csv":
            with open(file_path) as output:
                reader = csv.DictReader(output)
                file_as_array = [item for item in reader]
                if report_type == "simples":
                    return SimpleReport.generate(file_as_array)
                else:
                    return CompleteReport.generate(file_as_array)
        elif file_extension == "json":
            with open(file_path) as output:
                file_as_array = json.load(output)
                if report_type == "simples":
                    return SimpleReport.generate(file_as_array)
                else:
                    return CompleteReport.generate(file_as_array)

        else:
            with open(file_path) as output:
                file_as_array = xmltodict.parse(output.read())["dataset"][
                    "record"
                ]
                if report_type == "simples":
                    return SimpleReport.generate(file_as_array)
                else:
                    return CompleteReport.generate(file_as_array)
