from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __iter__(self):
        """Retorna o iterador a partir da coleção de livros em estoque.
        Equivalente ao método iterator "ConcreteAgreggator" do diagrama.
        """
        return InventoryIterator(self.data)

    def generate_report(self, content_list, report_type):
        if report_type == "simples":
            return SimpleReport.generate(content_list)
        elif report_type == "completo":
            return CompleteReport.generate(content_list)

    def import_data(self, file_path, report_type):
        new_content = self.importer.import_data(file_path)
        self.data.extend(new_content)
        return self.generate_report(self.data, report_type)
