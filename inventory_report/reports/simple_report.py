from datetime import date, datetime
from operator import itemgetter


def split_string_date(string_date):
    return string_date.split('-')


def convert_string_date_to_datetime(string_date):
    split_in_pieces = list(map(int, split_string_date(string_date)))

    converted_to_date = date(*split_in_pieces)

    return converted_to_date


class SimpleReport:

    @staticmethod
    def generate(products):
        products_count = {}
        earliest_production_date = None
        max_due_date = None


        for product in products:
            props_to_get = ['nome_da_empresa', 'data_de_fabricacao', 'data_de_validade']
            company, production_date, due_date = itemgetter(*props_to_get)(product)

            products_count[company] = (
                products_count[company] + 1 if company in products_count else 1
            )

            dates_to_compare = [production_date, due_date]
            production_date_datetime, due_date_datetime = list(
                map(convert_string_date_to_datetime, dates_to_compare)
            )

            earliest_production_date = min(
                [earliest_production_date, production_date_datetime]
            ) if earliest_production_date else production_date_datetime

            present = datetime.now()
            due_date_is_past_today = due_date_datetime > present.date()

            if due_date_is_past_today:
                max_due_date = min(
                    [due_date_datetime, max_due_date]
                ) if max_due_date else due_date_datetime

        answer_pieces = [
            f"Data de fabricação mais antiga: {earliest_production_date.isoformat()}",
            f"Data de validade mais próxima: {max_due_date.isoformat()}",
            f"Empresa com maior quantidade de produtos estocados: {max(products_count)}\n"
        ]

        answer = '\n'.join(answer_pieces)

        return answer
