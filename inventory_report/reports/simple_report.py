from collections import Counter
from datetime import datetime

data = [
        {
            "id": 1,
            "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim",
        },
        {
            "id": 2,
            "nome_do_produto": "sodium ferric gluconate complex",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2020-05-31",
            "data_de_validade": "2023-01-17",
            "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
            "instrucoes_de_armazenamento": "duis bibendum morbi",
        },
        {
            "id": 3,
            "nome_do_produto": "Dexamethasone Sodium Phosphate",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2019-09-13",
            "data_de_validade": "2023-02-13",
            "numero_de_serie": "BA52 2034 8595 7904 7131",
            "instrucoes_de_armazenamento": "morbi quis tortor id",
        },
        {
            "id": 4,
            "nome_do_produto": "Uricum acidum, Benzoicum acidum",
            "nome_da_empresa": "Newton Laboratories, Inc.",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
      ]


class SimpleReport:
    def oldest_date(products_list):
        manufacturing_date = []
        for product in products_list:
            manufacturing_date.append(product["data_de_fabricacao"])
            manufacturing_date.sort()
        old_date = manufacturing_date[0]
        return old_date

    def nearest_expiration(products_list):
        expiration_date = []
        today = '2021-05-25'
        formated_date = datetime.strptime(today, '%Y-%m-%d')
        for product in products_list:
            expiration_date.append(product["data_de_validade"])
            expiration_date.sort()
        for date in expiration_date:
            if date < today:
                expiration_date.remove(date)
        nearest_date = min(
            expiration_date, key=lambda x: abs(
                datetime.strptime(x, '%Y-%m-%d') - formated_date
            )
        )
        return nearest_date

    def repeated_company(products_list):
        company = []
        for product in products_list:
            company.append(product["nome_da_empresa"])
        occurrences = Counter(company)
        most_repeated = occurrences.most_common(1)[0][0]
        return most_repeated

    @staticmethod
    def generateReport(products_list):
        oldest = SimpleReport.oldest_date(products_list)
        nearest = SimpleReport.nearest_expiration(products_list)
        repeated = SimpleReport.repeated_company(products_list)
        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {nearest}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{repeated}\n"
        )
