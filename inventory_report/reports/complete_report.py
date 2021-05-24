from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, produtos):
        simple_report = SimpleReport.generate(produtos)

        empresas = []
        for produto in produtos:
            empresas = [*empresas, produto["nome_da_empresa"]]

        counter = Counter(empresas)
        complete_report = "Produtos estocados por empresa: \n"
        for empresa in counter:
            complete_report += f"- {empresa}: {counter[empresa]}\n"

        return simple_report + "\n" + complete_report
