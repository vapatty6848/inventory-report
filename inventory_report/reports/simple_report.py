from collections import Counter
from datetime import date


class SimpleReport:
    @staticmethod
    def generate(products_list):
        date_today = date.today()
        base_date = 10000
        data_fabricacao = "2021-05-20"
        data_validade = "1900-01-01"
        nome_empresa = []
        data_validade = '1990-05-20'
        for product in products_list:
            if(product["data_de_fabricacao"] < data_fabricacao):
                data_fabricacao = product["data_de_fabricacao"]
            validate = product["data_de_validade"].replace('-', ',').split(',')
            year = int(validate[0])
            month = int(validate[1])
            day = int(validate[2])
            difference = date(year, month, day) - date_today
            if(difference.days < base_date) and (difference.days > 0):
                data_validade = product["data_de_validade"]
                base_date = difference.days
            nome_empresa.append(product["nome_da_empresa"])

        most_commom_company = Counter(nome_empresa).most_common(1)[0][0]
        line1 = f"Data de fabricação mais antiga: {data_fabricacao}"
        line2 = f"Data de validade mais próxima: {data_validade}"
        line3 = "Empresa com maior quantidade de produtos estocados: "
        return f"{line1}\n{line2}\n{line3}{most_commom_company}\n"
