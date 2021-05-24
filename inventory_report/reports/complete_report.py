from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, inventory):
        simple = super().generate(inventory)

        counter = Counter(item['nome_da_empresa'] for item in inventory)
        stock = ""

        for c in counter:
            stock = stock + f'- {c}: {counter[c]}\n'

        full_report = (
            f"{simple}\n"
            f"Produtos estocados por empresa: \n"
            f"{stock}"
        )

        return full_report
