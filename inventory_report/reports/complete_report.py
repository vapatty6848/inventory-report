from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(self, report):
        simple_report = SimpleReport.generate(report)
        companies = [company["nome_da_empresa"] for company in report]
        count = Counter(companies)
        initial_stock = ''
        for count_company in count:
            initial_stock += f"- {count_company}: {count[count_company]}\n"
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{initial_stock}"
        )
