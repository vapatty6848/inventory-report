from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(InventoryIterator):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_path, import_type):
        self.import_type = import_type
        new_data = self.importer.import_data(file_path)
        self.data = [*self.data, *new_data]

    def generate_report(self):
        products = self.data

        simple_method = self.import_type == "simples"
        Reporter = SimpleReport if simple_method else CompleteReport

        answer = Reporter.generate(products)

        return answer
