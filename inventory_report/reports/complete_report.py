from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(list):

        return (
          f"{SimpleReport.generate(list)}\n"
          f"Produtos estocados por empresa: \n"
          f"{CompleteReport.counter(list)}"
        )

    def counter(list):
        companies = [item["nome_da_empresa"] for item in list]
        ocurrencies = Counter(companies)
        qtyByCompany = ""
        for key in ocurrencies:
            qtyByCompany += f"- {key}: {ocurrencies[key]}\n"
        return qtyByCompany
