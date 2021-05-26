from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(self, produtos):
        fabricacao_mais_antiga = str(min(
             datetime.strptime(produto["data_de_fabricacao", "%Y-%m-%d"])
             for produto in produtos
         ).date())

        proxima_validade = str(min(
            datetime.strptime(produto["data_de_validade", "%Y-%m-%d"])
            for produto in produtos
            if datetime.strptime(produto["data_de_validade"], "%Y-%m-%d")
            > datetime.today()
            ).date())

        maior_estoque = max(produto["nome_da_empresa"] for produto in produtos)

        relatorio = (
            + f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
            + f"Data de validade mais próxima: {proxima_validade}\n"
            "Empresa com maior quantidade de produtos estocados: "
            + f"{maior_estoque}\n"
        )
        return relatorio
