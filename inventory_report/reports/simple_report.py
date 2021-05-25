from datetime import datetime
from collections import Counter
from abc import ABC


class SimpleReport(ABC):
    @staticmethod
    def generate(list):
        oldestManufacturingdate = min(
            [item["data_de_fabricacao"] for item in list]
        )

        today = datetime.today()

        minExpirationDate = min(
            [item["data_de_validade"] for item in list
                if datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
                >= today]
        )

        companyMoreProducts = SimpleReport.companyMoreProducts(list)

        return (
            f"Data de fabricação mais antiga: {oldestManufacturingdate}\n"
            f"Data de validade mais próxima: {minExpirationDate}\n"
            f"Empresa com maior quantidade de produtos "
            f"estocados: {companyMoreProducts}\n"
        )

    def companyMoreProducts(list):
        companies = []
        [companies.append(item["nome_da_empresa"]) for item in list]
        data = Counter(companies)
        return data.most_common(1)[0][0]
