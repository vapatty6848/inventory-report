from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def __init__(self):
        print("Complete Report criado")

    @classmethod
    def generate(cls, products):
        simple_report = super().generate(products)
        companies_stock_counter = Counter()
        for product in products:
            companies_stock_counter[product["nome_da_empresa"]] += 1

        companies_stock = simple_report
        companies_stock += "\nProdutos estocados por empresa: \n"
        for company, quantity in companies_stock_counter.items():
            companies_stock += f"- {company}: {quantity}\n"

        return companies_stock
