from collections import Counter
from datetime import datetime


def get_company_with_most_items(stock):
    return max(
        Counter([stock_item["nome_da_empresa"] for stock_item in stock])
    )


def get_oldest_fabrication_date(stock):
    return min([stock_item["data_de_fabricacao"] for stock_item in stock])


def get_time_differece(today, date):
    print(today)
    # print(date)
    if today > date:
        print(today - date)
    else:
        print(date - today)


def get_nearest_expire_date(stock):
    today = str(datetime.now())

    nearest_expire_date = min(
        [
            stock_item["data_de_validade"]
            for stock_item in stock
            if stock_item["data_de_validade"] >= today
        ]
    )

    return nearest_expire_date
