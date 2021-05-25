import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(self, pathfile, type_report):
        if pathfile[len(pathfile) - 1] == 'v':
            with open(pathfile) as file:
                reporter_csv = csv.DictReader(file)
                reporter = []
                for row in reporter_csv:
                    reporter.append(row)

                if type_report == 'simples':
                    return SimpleReport.generate(reporter)
                else:
                    return CompleteReport.generate(reporter)

        else:
            with open(pathfile) as file:
                content = file.read()
                reporter_json = json.loads(content)

                if type_report == 'simples':
                    return SimpleReport.generate(reporter_json)
                else:
                    return CompleteReport.generate(reporter_json)


# print(Inventory.import_data('/home/cleyton/Documents/Projects/computer-science/sd-06-inventory-report/inventory_report/data/inventory.json', 'simples'))
