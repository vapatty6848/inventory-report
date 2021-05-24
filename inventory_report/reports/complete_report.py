from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(lista_produtos):
        return (
            f"{SimpleReport.generate(lista_produtos)}\n"
            f"Produtos estocados por empresa: \n"
            f"{CompleteReport.produtos_empresa(lista_produtos)}"
        )

    def produtos_empresa(lista_produtos):
        empresas = [produto["nome_da_empresa"] for produto in lista_produtos]
        ocorrencias = Counter(empresas)
        quantidades_por_empresa = ""

        for key in ocorrencias:
            quantidades_por_empresa += f"- {key}: {ocorrencias[key]}\n"
        return quantidades_por_empresa
