import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def csv(self, path):
        with open(path) as file:
            status_reader = csv.reader(file, delimiter=",", quotechar='"')
            headers, *data = status_reader
        array = []
        for values in data:
            obj = {}
            for index, header in enumerate(headers):
                obj[header] = values[index]
            array.append(obj)
        return array

    @classmethod
    def json(self, path):
        with open(path) as file:
            content = file.read()  # leitura do arquivo
        data = json.loads(content)
        return data

    @classmethod
    def xml(self, path):
        with open(path) as file:
            xpars = xmltodict.parse(file.read())
        res_json = json.dumps(xpars)
        return json.loads(res_json)["dataset"]["record"]

    @classmethod
    def identify_path(self, path):
        file_type = path.split(".")[-1]

        if file_type == "csv":
            return self.csv(path)
        if file_type == "json":
            return self.json(path)
        if file_type == "xml":
            return self.xml(path)

    @classmethod
    def import_data(self, path, type):
        array = self.identify_path(path)
        if type == "simples":
            return SimpleReport.generate(array)
        elif type == "completo":
            return CompleteReport.generate(array)
