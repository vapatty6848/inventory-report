from collections import Counter
from datetime import datetime


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

    @classmethod
    def generate(cls, products_list):
        omd = SimpleReport.oldest_manufact_date(products_list)
        ned = SimpleReport.nearest_expiration_date(products_list)
        mrc = SimpleReport.most_repeated_company(products_list)
        return (
            f"Data de fabricação mais antiga: {omd}\n"
            f"Data de validade mais próxima: {ned}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{mrc}\n"
        )
