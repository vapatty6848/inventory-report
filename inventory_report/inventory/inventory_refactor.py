from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, strategy):
        self._strategy = strategy
        self._iterable_data = []

    def import_data(self, path, version):
        self._iterable_data = self._strategy.import_data(path)
        # self._iterable_data.append(list_inventory)

        report = (
            CompleteReport.generate(self._iterable_data)
            if version == "completo"
            else SimpleReport.generate(self._iterable_data)
        )
        return report

    def __iter__(self):
        return InventoryIterator(self._iterable_data)


csv_instance = InventoryRefactor(CsvImporter)
print(csv_instance.import_data('inventory_report/data/inventory.csv', 'completo'))
json_instance = InventoryRefactor(JsonImporter)
xml_instance = InventoryRefactor(XmlImporter)
