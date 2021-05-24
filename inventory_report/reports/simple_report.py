from datetime import datetime


class SimpleReport:
    @classmethod
    def oldest_product(cls, inventory_list):
        return sorted(
            inventory_list, key=lambda k: k["data_de_fabricacao"]
        )[0]["data_de_fabricacao"]

    @classmethod
    def earlier_expire_date(cls, inventory_list):
        valid_products = []

        for product in inventory_list:
            expire_date = datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            )
            if expire_date > datetime.today():
                valid_products.append(product)

        return sorted(
            valid_products, key=lambda k: k["data_de_validade"]
        )[0]["data_de_validade"]

    @classmethod
    def most_products(cls, inventory_list):
        companies = [product["nome_da_empresa"] for product in inventory_list]
        most_frequent = ""
        biggest_counter = 0

        for _ in companies:
            counter = 0
            for product in inventory_list:
                counter = companies.count(product["nome_da_empresa"])
                if counter > biggest_counter:
                    most_frequent = product["nome_da_empresa"]
                    biggest_counter = counter

        return most_frequent

    @classmethod
    def generate(cls, inventory):
        oldest = cls.oldest_product(inventory)
        earlier = cls.earlier_expire_date(inventory)
        most = cls.most_products(inventory)

        line1 = f"Data de fabricação mais antiga: {oldest}\n"
        line2 = f"Data de validade mais próxima: {earlier}\n"
        line3 = f"Empresa com maior quantidade de produtos estocados: {most}\n"

        return f"{line1}{line2}{line3}"


if __name__ == "__main__":
    list_prod = [
        {
            "id": 1,
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2020-02-09",
        },
        {
            "id": 2,
            "nome_da_empresa": "Forces of",
            "data_de_fabricacao": "2010-07-04",
            "data_de_validade": "2023-02-09",
        },
        {
            "id": 3,
            "nome_da_empresa": "Nature",
            "data_de_fabricacao": "2021-07-04",
            "data_de_validade": "2021-12-09",
        },
        {
            "id": 4,
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2021-07-04",
            "data_de_validade": "2020-12-09",
        },
    ]

    report = SimpleReport(list_prod)
    report.generate()
