from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


# Requisito 2
class CompleteReport(SimpleReport):
    def __init__(self):
        SimpleReport.__init__(self)

    def stocked_products_by_company(self, products_list):
        companies = []
        for product in products_list:
            companies.append(product["nome_da_empresa"])
        occurence_count = Counter(companies)
        formated_strings = ""
        for company in occurence_count:
            formated_strings += f"- {company}: {occurence_count[company]}\n"
        return formated_strings

    @classmethod
    def generate(cls, products_list):
        sg = super().generate(products_list)
        cs = CompleteReport.stocked_products_by_company(cls, products_list)
        return (
            f"{sg}\n"
            f"Produtos estocados por empresa: \n"
            f"{cs}"
        )
