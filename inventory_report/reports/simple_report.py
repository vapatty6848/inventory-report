from datetime import date


class SimpleReport:
    @classmethod
    def generate(cls, inventory):
        date_today = str(date.today())

        oldest_item = min([item["data_de_fabricacao"] for item in inventory])
        product_validate = min(
          [
            item["data_de_validade"]
            for item in inventory
            if item["data_de_validade"] >= date_today
          ]
        )
        max_company = max(item["nome_da_empresa"] for item in inventory)

        return (
          f"Data de fabricação mais antiga: {oldest_item}\n"
          f"Data de validade mais próxima: {product_validate}\n"
          f"Empresa com maior quantidade de produtos estocados: "
          f"{max_company}\n"
        )
