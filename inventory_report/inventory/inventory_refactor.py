from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    @classmethod
    def identify_path(self, path):
        file_type = path.split(".")[-1]

        if file_type == "csv":
            return CsvImporter.import_data(path)
        if file_type == "json":
            return JsonImporter.import_data(path)
        if file_type == "xml":
            return XmlImporter.import_data(path)

    @classmethod
    def import_data(self, path, type):
        array = self.identify_path(path)
        if type == "simples":
            return SimpleReport.generate(array)
        elif type == "completo":
            return CompleteReport.generate(array)
