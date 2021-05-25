from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, strategy):
        self.importer = strategy
        self.data = []

    def import_data(self, path, version):
        list_inventory = self.importer.import_data(path)
        self.data.extend(list_inventory)

        report = (
            CompleteReport.generate(self.data)
            if version == "completo"
            else SimpleReport.generate(self.data)
        )
        return report

    def __iter__(self):
        return InventoryIterator(self.data)
