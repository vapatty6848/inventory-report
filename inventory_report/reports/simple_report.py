from datetime import datetime


class SimpleReport:
    # @classmethod criar métodos que pertençam à classe, e não ao objeto
    @classmethod
    # cls - referência explícita à classe
    def generate(cls, date_or_name):
        # (1)
        today_date = datetime.today().strftime('%Y-%m-%d')

        oldest_manufacturing_date = min(
          [manufacturing_date[
            "data_de_fabricacao"] for manufacturing_date in date_or_name]
        )
        # (2 - "min" Devolve o menor item de um iterável
        # ou o menor de dois ou mais argumentos)
        closest_expiration_date = min(
            [
                expiration_date["data_de_validade"]
                for expiration_date in date_or_name
                if expiration_date["data_de_validade"] >= today_date
            ]
        )
        # ( 3 - "max" Devolve o maior item em um iterável
        # ou o maior de dois ou mais argumentos.
        quantity_of_stocked_products = max(
          company_name["nome_da_empresa"]
          for company_name in date_or_name)

        return (
          f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
          f"Data de validade mais próxima: {closest_expiration_date}\n"
          "Empresa com maior quantidade de produtos "
          f"estocados: {quantity_of_stocked_products}\n"
        )
# Notas de Rodapé
# 1(https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python)
# 2(https://www.tutorialspoint.com/python/list_min.htm) - vide 3
# 3(https://docs.python.org/pt-br/3/library/functions.html?highlight=min#min)
