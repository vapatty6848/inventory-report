import re
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __init__(
        self,
        path='/home/danielmjales/Desktop/trybe/projects/sd-06-inventory-report/inventory_report/data/inventory.xml',
        reportType='naLA'
    ):
        self.path = path
        self.reportType = reportType

    def _checkPath(self):
        reCSV = re.compile(r"csv$")
        reJSON = re.compile(r"json$")
        reXML = re.compile(r"xml$")
        if reCSV.search(self.path):
            csvImporter = CsvImporter(self.path)
            return csvImporter.data_import()
        if reJSON.search(self.path):
            jsonImporter = JsonImporter(self.path)
            return jsonImporter.data_import()
        if reXML.search(self.path):
            xmlImporter = XmlImporter(self.path)
            return xmlImporter.data_import()

    def import_data(self):
        listOfdicts = self._checkPath()
        if self.reportType == 'simples':
            simpleReport = SimpleReport(listOfdicts)
            simpleReport.generate()
        else:
            completeReport = CompleteReport(listOfdicts)
            completeReport.generate()
