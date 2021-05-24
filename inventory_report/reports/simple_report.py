from datetime import datetime


def get_oldest(my_list):
    oldest = datetime.strptime(my_list[0]["data_de_fabricacao"], "%Y-%m-%d")
    for item in my_list:
        item_date = datetime.strptime(item["data_de_fabricacao"], "%Y-%m-%d")
        if item_date < oldest:
            oldest = item_date
    return oldest.date()


def get_next_to_expire(my_list):
    current_date = datetime.now()
    next_expire = datetime.strptime(
        my_list[0]["data_de_validade"], "%Y-%m-%d"
    )
    lowest_diff = next_expire - current_date

    for item in my_list:
        item_date = datetime.strptime(
            item["data_de_validade"], "%Y-%m-%d"
        )
        if item_date > current_date and lowest_diff > (
            item_date - current_date
        ):
            lowest_diff = current_date - item_date
            next_expire = item_date

    return next_expire.date()


def get_largest_stock(my_list):
    companies_list = {}
    for item in my_list:
        company = item["nome_da_empresa"]
        companies_list.setdefault(company, 0)
        companies_list[company] += 1

    companies_sort = sorted(companies_list, reverse=True)
    return str(companies_sort[0])


class SimpleReport:
    @classmethod
    def generate(cls, list):
        oldest = get_oldest(list)
        next_to_expire = get_next_to_expire(list)
        largest = get_largest_stock(list)
        simple_report = (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {next_to_expire}\n"
            f"Empresa com maior quantidade de produtos estocados: {largest}\n"
        )
        return simple_report
