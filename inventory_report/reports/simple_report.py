from datetime import date
from collections import Counter


def the_oldest_one(produtos):
    '''Retorna o produto mais antigo'''
    try:
        produtos_filtrados = (
            data_fabric["data_de_fabricacao"] for data_fabric in produtos
            )
        return min(produtos_filtrados)
    except ValueError:
        return print("Erro ao retornar o produto mais antigo")


def next_to_expire(produtos):
    '''Retorna o produto mais próximo de vencer'''
    try:
        produtos_filtrados = (
            data_validade["data_de_validade"] for data_validade in produtos
            if data_validade["data_de_validade"] > str(date.today())
        )
        return min(produtos_filtrados)
    except ValueError:
        return print("erro ao retornar o produto mais próximo de vencer")


def company_biggest_stocker(produtos):
    '''Retorna a empresa com maior estoque'''
    try:
        produtos_filtrados = Counter(
            nome_empresa["nome_da_empresa"] for nome_empresa in produtos
        )
        return produtos_filtrados.most_common(1)[0][0]
    except ValueError:
        return print("Erro ao retornar empresa maior estoque")


class SimpleReport:
    @classmethod
    def generate(self, produtos):
        '''Método generate monta o relatório simples'''
        mais_antigo = the_oldest_one(produtos)
        proximo_a_expirar = next_to_expire(produtos)
        empresa_maior_estoque = company_biggest_stocker(produtos)
        relatorio = (
            f"Data de fabricação mais antiga: {mais_antigo}\n"
            + f"Data de validade mais próxima: {proximo_a_expirar}\n"
            + "Empresa com maior quantidade de produtos estocados: "
            + f"{empresa_maior_estoque}\n"
        )
        return relatorio
