from datetime import datetime


class SimpleReport:
    def __init__(self):
        print("Simple Report criado")

    @classmethod
    def get_smallest_manufacturing_date(cls, products, date_pattern):
        return str(
            min(
                datetime.strptime(item["data_de_fabricacao"], date_pattern)
                for item in products
            ).date()
        )

    @classmethod
    def get_next_expire_date(cls, products, date_pattern):
        return str(
            min(
                datetime.strptime(item["data_de_validade"], date_pattern)
                for item in products
                if datetime.strptime(item["data_de_validade"], date_pattern)
                > datetime.today()
            ).date()
        )

    @classmethod
    def get_most_products_owner(cls, products):
        return max(item["nome_da_empresa"] for item in products)

    @classmethod
    def generate(cls, products):
        date_pattern = "%Y-%m-%d"
        smallest_manufacturing_date = cls.get_smallest_manufacturing_date(
            products, date_pattern
        )

        next_expire_date = cls.get_next_expire_date(products, date_pattern)

        most_products_owner = cls.get_most_products_owner(products)

        report = (
            f"Data de fabricação mais antiga: {smallest_manufacturing_date}\n"
            f"Data de validade mais próxima: {next_expire_date}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {most_products_owner}\n"
        )
        return report
