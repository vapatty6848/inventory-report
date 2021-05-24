from datetime import datetime
class SimpleReport:

    @staticmethod
    def generate(inventory):
        today = datetime.today()
        oldest_manufacture = min([product["data_de_fabricacao"] for product in inventory])
        next_valid = min([product["data_de_validade"] for product in inventory if datetime.strptime(product["data_de_validade"], "%Y-%m-%d") >= today])
        print(next_valid)
        company = max([product["nome_da_empresa"] for product in inventory])
        return (
            f"Data de fabricação mais antiga: {oldest_manufacture}\n"
            f"Data de validade mais próxima: {next_valid}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{company}\n"
        )

        