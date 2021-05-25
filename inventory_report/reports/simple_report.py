from datetime import datetime
import statistics


class SimpleReport:
    def generate(stock):
        now = str(datetime.now())
        data_de_fabricação_mais_antiga = [
            data_validade["data_de_fabricacao"] for data_validade in stock
        ]
        data_de_validade_mais_próxima = [
            data_validade["data_de_validade"]
            for data_validade in stock
            if data_validade["data_de_validade"] > now
        ]
        empresa_com_maior_quantidade_de_produtos_estocados = [
            produtos_estocados["nome_da_empresa"]
            for produtos_estocados in stock
        ]
        data_fabricacao = min(data_de_fabricação_mais_antiga)
        data_validade = min(data_de_validade_mais_próxima)
        empresa = statistics.mode(
            empresa_com_maior_quantidade_de_produtos_estocados
        )
        relatorio = f"""Data de fabricação mais antiga: {data_fabricacao}
Data de validade mais próxima: {data_validade}
Empresa com maior quantidade de produtos estocados: {empresa}
"""
        return relatorio
