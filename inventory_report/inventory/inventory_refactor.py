from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    @classmethod
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def import_data(self, path, report_type):
        self.data += self.importer.import_data(path)
        if report_type == "simples":
            report = SimpleReport.generate(self.data)
        else:
            report = CompleteReport.generate(self.data)
        return report

    def __iter__(self):
        return InventoryIterator(self.data)
