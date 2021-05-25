from collections import Counter
from datetime import date


class SimpleReport:
    @classmethod
    def products_per_company(cls, products_list):
        company_and_quantity = []
        for product in products_list:
            company_and_quantity.append(product["nome_da_empresa"])
        return Counter(company_and_quantity)

    @classmethod
    def generate(cls, products_list):
        date_today = date.today()
        base_date = 10000
        data_fabricacao = "2021-05-20"
        for product in products_list:
            if product["data_de_fabricacao"] < data_fabricacao:
                data_fabricacao = product["data_de_fabricacao"]
            validate = product["data_de_validade"].replace("-", ",").split(",")
            year = int(validate[0])
            month = int(validate[1])
            day = int(validate[2])
            date_difference = date(year, month, day) - date_today
            if (date_difference.days < base_date) and (
                date_difference.days > 0
            ):
                data_validade = product["data_de_validade"]
                base_date = date_difference.days

        list_of_companies = cls.products_per_company(products_list)
        most_common_company = list_of_companies.most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {data_fabricacao}\n"
            + f"Data de validade mais próxima: {data_validade}\n"
            + "Empresa com maior quantidade de produtos estocados: "
            + f"{most_common_company}\n"
        )
