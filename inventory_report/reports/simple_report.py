from datetime import datetime


class SimpleReport:
    def generate(list_data):
        today = datetime.today().strftime('%Y-%m-%d')
        older = min([info["data_de_fabricacao"] for info in list_data])
        closest = min([
            info["data_de_validade"] for info in list_data
            if info["data_de_validade"] > today
        ])
        name = max([info["nome_da_empresa"] for info in list_data])

        return (
            "Data de fabricação mais antiga: %s\n"
            "Data de validade mais próxima: %s\n"
            "Empresa com maior quantidade de produtos estocados: %s\n"
            % (older, closest, name)
        )
