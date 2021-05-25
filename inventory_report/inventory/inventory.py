from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def _call_importer(cls, file_path):
        extension = file_path.split('.')[-1]
        if extension == 'csv':
            return CsvImporter.import_data(file_path)
        elif extension == 'json':
            return JsonImporter.import_data(file_path)
        elif extension == 'xml':
            return XmlImporter.import_data(file_path)
        else:
            return None

    @classmethod
    def _generate_report(cls, content_list, report_type):
        if report_type == "simples":
            return SimpleReport.generate(content_list)
        elif report_type == "completo":
            return CompleteReport.generate(content_list)

    @classmethod
    def import_data(cls, file_path, report_type):
        content_list = cls._call_importer(file_path)
        return cls._generate_report(content_list, report_type)
