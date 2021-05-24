from datetime import date
from collections import Counter
from abc import ABC


class SimpleReport(ABC):
    @staticmethod
    def generate(lista_produtos):
        fabricacao = SimpleReport.data_fabricacao_antiga(lista_produtos)
        validade = SimpleReport.data_validade_proxima(lista_produtos)
        empresa = SimpleReport.empresa_maior_estoque(lista_produtos)

        return (
            f"Data de fabricação mais antiga: {fabricacao}\n"
            + f"Data de validade mais próxima: {validade}\n"
            + "Empresa com maior quantidade de produtos estocados: "
            f"{empresa}\n"
        )

    def data_validade_proxima(lista_produtos):
        data_atual = date.today()
        data_validade = []
        for produto in lista_produtos:
            if date.fromisoformat(produto["data_de_validade"]) > data_atual:
                data_validade.append(produto["data_de_validade"])
        data_validade.sort()
        return data_validade[0]

    def data_fabricacao_antiga(lista_produtos):
        data_fabricacao = []
        for produto in lista_produtos:
            data_fabricacao.append(produto["data_de_fabricacao"])
        data_fabricacao.sort()
        return data_fabricacao[0]

    def empresa_maior_estoque(lista_produtos):
        empresas = []
        for produto in lista_produtos:
            empresas.append(produto["nome_da_empresa"])
        ocorrencias = Counter(empresas)
        mais_frequente = ocorrencias.most_common(1)[0][0]
        return mais_frequente
