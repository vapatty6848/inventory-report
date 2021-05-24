import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def _generate_report(cls, content, report_type):
        if report_type == "simples":
            return SimpleReport.generate(content)
        elif report_type == "completo":
            return CompleteReport.generate(content)

    @classmethod
    def import_data(cls, file, report_type):
        content_list = []
        with open(file, newline='') as csvfile:
            content = csv.DictReader(csvfile, delimiter=",")
            for row in content:
                current = {}
                for key in row:
                    current[key] = row[key]
                content_list.append(current)

        return cls._generate_report(content_list, report_type)
