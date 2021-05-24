from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, inventory):
        simple_report = super().generate(inventory)
        companies = [company["nome_da_empresa"] for company in inventory]
        companies_list = Counter(companies)
        company_qtd = ""
        for company in companies_list:
            quantity = companies.count(company)
            company_qtd += f"- {company}: {quantity}\n"

        complet_report = (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{company_qtd}"
        )
        return complet_report
