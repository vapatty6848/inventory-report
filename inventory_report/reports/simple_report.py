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


# Requisito 1
class SimpleReport:

    def oldest_manufact_date(products_list):
        manufacturing_dates = []
        for product in products_list:
            manufacturing_dates.append(product["data_de_fabricacao"])
            manufacturing_dates.sort()
        oldest_date = manufacturing_dates[0]
        return oldest_date

    def nearest_expiration_date(products_list):
        expiration_dates = []
        now = '2021-05-24'
        formated_date = datetime.strptime(now, '%Y-%m-%d')
        for product in products_list:
            expiration_dates.append(product["data_de_validade"])
            expiration_dates.sort()
        for date in expiration_dates:
            if date < now:
                expiration_dates.remove(date)
        nearest_date = min(
            expiration_dates, key=lambda x: abs(
                datetime.strptime(x, '%Y-%m-%d') - formated_date
            )
        )
        return nearest_date

    def most_repeated_company(products_list):
        companies = []
        for product in products_list:
            companies.append(product["nome_da_empresa"])
        occurence_count = Counter(companies)
        most_repeated = occurence_count.most_common(1)[0][0]
        return most_repeated

    @staticmethod
    def generate(products_list):
        omd = SimpleReport.oldest_manufact_date(products_list)
        ned = SimpleReport.nearest_expiration_date(products_list)
        mrc = SimpleReport.most_repeated_company(products_list)
        return (
            f"Data de fabricação mais antiga: {omd}\n"
            f"Data de validade mais próxima: {ned}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{mrc}\n"
        )

    # @staticmethod
    # def generate(products_list):
    #     now = '2021-05-24'
    #     formated_date = datetime.strptime(now, '%Y-%m-%d')
    #     expiration_dates = []
    #     manufacturing_dates = []
    #     companies = []
    #     for product in products_list:
    #         expiration_dates.append(product["data_de_validade"])
    #         manufacturing_dates.append(product["data_de_fabricacao"])
    #         companies.append(product["nome_da_empresa"])
    #         manufacturing_dates.sort()
    #         expiration_dates.sort()

    #     print(type(expiration_dates[0]))
    #     print(type(now))

    #     for date in expiration_dates:
    #         if date < now:
    #             expiration_dates.remove(date)

    #     nearest_date = min(
    #         expiration_dates, key=lambda x: abs(
    #             datetime.strptime(x, '%Y-%m-%d') - formated_date
    #         )
    #     )
    #     occurence_count = Counter(companies)
    #     most_frequent_in_stock = occurence_count.most_common(1)[0][0]

    #     return (
    #         f"Data de fabricação mais antiga: {manufacturing_dates[0]}\n"
    #         f"Data de validade mais próxima: {nearest_date}\n"
    #         f"Empresa com maior quantidade de produtos estocados: "
    #         f"{most_frequent_in_stock}\n"
    #     )
