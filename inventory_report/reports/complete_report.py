from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, inventory):
        simple_report = super().generate(inventory)

        counter = Counter(item["nome_da_empresa"] for item in inventory)
        full_stock = ""

        for c in counter:
            full_stock = full_stock + f'- {c}: {counter[c]}\n'

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{full_stock}"
          )
