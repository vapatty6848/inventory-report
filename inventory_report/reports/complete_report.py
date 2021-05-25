from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self):
        SimpleReport.__init__(self)

    def empresas_estoque(self, products_list):
        empresas = []
        for product in products_list:
            empresas.append(product["nome_da_empresa"])
        count_empresa = Counter(empresas)
        resposta_string = ""
        for company in count_empresa:
            resposta_string += f"- {company}: {count_empresa[company]}\n"
        return resposta_string

    @classmethod
    def generate(cls, products_list):
        simplereportawnser = super().generate(products_list)
        completereportawnser = CompleteReport.empresas_estoque(
          cls, products_list
        )
        return (
            f"{simplereportawnser}\n"
            f"Produtos estocados por empresa: \n"
            f"{completereportawnser}"
        )
