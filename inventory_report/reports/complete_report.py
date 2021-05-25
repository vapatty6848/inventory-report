from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


def company_stock_list(produtos):
    '''Gera a lista de produtos estocados por empresa'''
    try:
        relatorio = ""
        empresas = Counter(
            nome_empresa["nome_da_empresa"] for nome_empresa in produtos
        )
        for empresa in empresas:
            relatorio += f"- {empresa}: {empresas[empresa]}\n"
        return relatorio
    except ValueError:
        return print("Erro ao gerar lista de produtos estocados por empresa")


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, produtos):
        '''Método generate monta o relatório completo'''
        relatorio_simples = SimpleReport.generate(produtos)
        relatorio_de_estoque = company_stock_list(produtos)
        relatorio_completo = (
            f"{relatorio_simples}\n"
            + "Produtos estocados por empresa: \n"
            + f"{relatorio_de_estoque}"
        )
        return relatorio_completo
