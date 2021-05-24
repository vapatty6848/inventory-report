from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, inventory):
        today = datetime.today()
        cls.oldest_manufacture = min(
            [product["data_de_fabricacao"] for product in inventory]
        )
        cls.closest_expiration_date = min(
            [
                product["data_de_validade"]
                for product in inventory
                if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                >= today
            ]
        )
        cls.company = max(
            [product["nome_da_empresa"] for product in inventory]
        )

        return (
            f"Data de fabricação mais antiga: {cls.oldest_manufacture}\n"
            f"Data de validade mais próxima: {cls.closest_expiration_date }\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{cls.company}\n"
        )
