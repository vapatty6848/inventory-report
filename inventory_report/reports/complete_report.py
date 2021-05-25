from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, date_or_products):
        # super() - Função embutida - Vide 1
        simple_report = super().generate(date_or_products)

        company_name = [name["nome_da_empresa"] for name in date_or_products]

        # Counter() Contagens convenientes e rápidas - Vide 2
        counter_companies = Counter(company_name)

        quantity_product_company = ""
        for company in counter_companies:
            # count() - Retorna o número de ocorrências da sub-string - Vide 3
            quantity_products = company_name.count(company)
            quantity_product_company += f"- {company}: {quantity_products}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{quantity_product_company}"
        )
# 1 - super()
# https://docs.python.org/pt-br/3/library/functions.html?highlight=super#super
# 2 - Counter
# https://docs.python.org/pt-br/3/library/collections.html?highlight=counter#collections.Counter
# 3 - count()
# https://docs.python.org/pt-br/3/library/stdtypes.html?highlight=count#str.count
