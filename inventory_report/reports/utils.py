from datetime import datetime


class ReportsUtils:
    @classmethod
    def get_oldest(cls, my_list):
        oldest = datetime.strptime(
            my_list[0]["data_de_fabricacao"], "%Y-%m-%d"
        )
        for item in my_list:
            item_date = datetime.strptime(
                item["data_de_fabricacao"], "%Y-%m-%d"
            )
            if item_date < oldest:
                oldest = item_date
        return oldest.date()

    @classmethod
    def get_next_to_expire(cls, my_list):
        current_date = datetime.now()
        next_expire = datetime.strptime(
            my_list[0]["data_de_validade"], "%Y-%m-%d"
        )
        lowest_diff = next_expire - current_date

        for item in my_list:
            item_date = datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
            if item_date > current_date and lowest_diff > (
                item_date - current_date
            ):
                lowest_diff = current_date - item_date
                next_expire = item_date

        return next_expire.date()

    @classmethod
    def get_stock(cls, my_list):
        companies_list = {}
        for item in my_list:
            company = item["nome_da_empresa"]
            companies_list.setdefault(company, 0)
            companies_list[company] += 1

        return companies_list

    @classmethod
    def get_largest_stock(cls, my_list):
        companies_list = cls.get_stock(my_list)
        companies_sort = sorted(companies_list, reverse=True)
        return str(companies_sort[0])