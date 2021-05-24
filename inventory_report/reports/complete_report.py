from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, report):
        simple_report = SimpleReport.generate(report)
        company = [compny["nome_da_empresa"] for compny in report]
        count = Counter(company)
        initial_stock = ''
        for cia in count:
            initial_stock += f"- {cia}: {count[cia]}\n"
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{initial_stock}"
        )