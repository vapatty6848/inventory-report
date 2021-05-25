from statistics import mode
from datetime import datetime


class SimpleReport:    
    def generate(self, data):
        date_now = datetime.now()
        nomes_das_empresas = []
        datas_de_fabricacao = []
        datas_de_validade = []
        for product in data:
            nomes_das_empresas.append(product["nome_da_empresa"])
            datas_de_fabricacao.append(product["data_de_fabricacao"])
            validade = product["data_de_validade"]
            if datetime.strptime(validade, "%Y-%m-%d") >= date_now:
                datas_de_validade.append(validade)
        datas_de_fabricacao.sort(
          key=lambda date: datetime.strptime(date, "%Y-%m-%d")
        )
        datas_de_validade.sort(
          key=lambda date: datetime.strptime(date, "%Y-%m-%d")
        )
        empresa_maior_quantidade = mode(nomes_das_empresas)
        return (
            f"Data de fabricação mais antiga: {datas_de_fabricacao[0]}" +
            f"\nData de validade mais próxima: {datas_de_validade[0]}" +
            "\nEmpresa com maior quantidade de " +
            f"produtos estocados: {empresa_maior_quantidade}\n"
        )

# print(SimpleReport().generate([
#   {
#       "id": 1,
#       "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
#       "nome_da_empresa": "Forces of Nature",
#       "data_de_fabricacao": "2020-07-04",
#       "data_de_validade": "2023-02-09",
#       "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#       "instrucoes_de_armazenamento": "in blandit ultrices enim",
#   },
#   {
#       "id": 2,
#       "nome_do_produto": "sodium ferric gluconate complex",
#       "nome_da_empresa": "Forces of Nature",
#       "data_de_fabricacao": "2020-05-31",
#       "data_de_validade": "2023-01-17",
#       "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
#       "instrucoes_de_armazenamento": "duis bibendum morbi",
#   },
#   {
#       "id": 3,
#       "nome_do_produto": "Dexamethasone Sodium Phosphate",
#       "nome_da_empresa": "sanofi-aventis U.S. LLC",
#       "data_de_fabricacao": "2019-09-13",
#       "data_de_validade": "2023-02-13",
#       "numero_de_serie": "BA52 2034 8595 7904 7131",
#       "instrucoes_de_armazenamento": "morbi quis tortor id",
#   },
#   {
#       "id": 4,
#       "nome_do_produto": "Uricum acidum, Benzoicum acidum",
#       "nome_da_empresa": "Newton Laboratories, Inc.",
#       "data_de_fabricacao": "2019-11-08",
#       "data_de_validade": "2019-11-24",
#       "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
#       "instrucoes_de_armazenamento": "velit eu est congue elementum",
#   },
# ]))