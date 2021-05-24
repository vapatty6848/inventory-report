import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        with open(file_path) as output:
            reader = csv.DictReader(output)
            file_as_array = [item for item in reader]
            if report_type == "simples":
                return SimpleReport.generate(file_as_array)
            else:
                return CompleteReport.generate(file_as_array)


print(Inventory.import_data("inventory_report/data/inventory.csv", "simples"))
