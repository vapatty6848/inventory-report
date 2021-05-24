from datetime import date


class SimpleReport:
    @classmethod
    def generate(cls, inventory):
        today = str(date.today())

        oldest = min([item["data_de_fabricacao"] for item in inventory])
        validade = min(
            [
                item["data_de_validade"]
                for item in inventory
                if item["data_de_validade"] >= today
            ]
        )
        max_company = max(item["nome_da_empresa"] for item in inventory)

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {validade}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{max_company}\n"
        )
