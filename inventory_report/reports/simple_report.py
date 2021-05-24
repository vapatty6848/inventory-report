from datetime import date
from collections import Counter


def counter(products):
    companies = Counter(
        name["nome_da_empresa"] for name in products
    ).most_common(1)
    return companies


class SimpleReport:
    @classmethod
    def generate(self, products_list):
        oldest = min(
            data_fabrica["data_de_fabricacao"]
            for data_fabrica in products_list
        )
        next_to_expire = min(
            data_validade["data_de_validade"]
            for data_validade in products_list
            if data_validade["data_de_validade"] > str(date.today())
        )
        stock_counter = counter(products_list)
        fab_date = f"Data de fabricação mais antiga: {oldest}\n"
        valid_date = f"Data de validade mais próxima: {next_to_expire}\n"
        stock_quantity = "Empresa com maior quantidade de produtos estocados:"
        return (
          f"{fab_date}{valid_date}{stock_quantity} {stock_counter[0][0]}\n"
        )
        