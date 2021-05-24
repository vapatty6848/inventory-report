from datetime import datetime
from collections import Counter

# dict_list = [
#         {
#             "id": 1,
#             "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
#             "nome_da_empresa": "Forces of Nature",
#             "data_de_fabricacao": "2020-07-04",
#             "data_de_validade": "2023-02-09",
#             "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#             "instrucoes_de_armazenamento": "in blandit ultrices enim",
#         },
#         {
#             "id": 2,
#             "nome_do_produto": "sodium ferric gluconate complex",
#             "nome_da_empresa": "sanofi-aventis U.S. LLC",
#             "data_de_fabricacao": "2020-05-31",
#             "data_de_validade": "2023-01-17",
#             "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
#             "instrucoes_de_armazenamento": "duis bibendum morbi",
#         },
#         {
#             "id": 3,
#             "nome_do_produto": "Dexamethasone Sodium Phosphate",
#             "nome_da_empresa": "sanofi-aventis U.S. LLC",
#             "data_de_fabricacao": "2019-09-13",
#             "data_de_validade": "2023-02-13",
#             "numero_de_serie": "BA52 2034 8595 7904 7131",
#             "instrucoes_de_armazenamento": "morbi quis tortor id",
#         },
#         {
#             "id": 4,
#             "nome_do_produto": "Uricum acidum, Benzoicum acidum",
#             "nome_da_empresa": "Newton Laboratories, Inc.",
#             "data_de_fabricacao": "2019-11-08",
#             "data_de_validade": "2019-11-25",
#             "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
#             "instrucoes_de_armazenamento": "velit eu est congue elementum",
#         },
#     ]


class SimpleReport:
    # def __init__(self):
    @staticmethod
    def generate(dict_list):
        dates_of_creation = []
        dates_of_expiration = []
        company_names = []

        for date in dict_list:
            dates_of_creation.append(date["data_de_fabricacao"])
            dates_of_expiration.append(date["data_de_validade"])
            company_names.append(date["nome_da_empresa"])

        dates_of_creation.sort(
            key=lambda date: datetime.strptime(date, "%Y-%m-%d")
        )
        oldest_creation = dates_of_creation[0].strip()

        dates_of_expiration.sort(
            key=lambda date: datetime.strptime(date, "%Y-%m-%d")
        )

        current_year = datetime.now().date().strftime("%Y")

        for date in dates_of_expiration:
            if current_year >= date[0:4]:
                dates_of_expiration.remove(date)

        closest_expiration = dates_of_expiration[0].strip()

        company_list = Counter(company_names)
        inventory = company_list.most_common()[0][0].strip()

        r1 = f"Data de fabricação mais antiga: {oldest_creation}"

        r2 = f"Data de validade mais próxima: {closest_expiration}"

        r3 = f"Empresa com maior quantidade de produtos estocados: {inventory}"

        report = f"{r1}\n{r2}\n{r3}\n"

        return report


# SimpleReport.generate(dict_list)
