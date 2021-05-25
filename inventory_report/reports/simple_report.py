import json
from datetime import datetime

phrase3 = "Empresa com maior quantidade de produtos estocados"


def generate(data):
    date_format = "%Y-%m-%d"
    today = datetime.now().strftime(date_format)
    today_parse = datetime.strptime(today, date_format)
    index = 0
    with open(data) as json_file:
        all_product_list = json.load(json_file)
        get_company_names = [
            name['nome_da_empresa'] for name in all_product_list]
        company_name_max = max(get_company_names)
        for each_product in all_product_list:
            oldest_product = datetime.strptime(
                each_product['data_de_validade'], date_format)
            oldest_manufacture = datetime.strptime(
                each_product['data_de_fabricacao'], date_format)
            if index == 0:
                difference_product = oldest_product - today_parse
                old_date = each_product['data_de_validade']
                difference_manufacture = today_parse - oldest_manufacture
                old_manufacture = each_product['data_de_fabricacao']
            if oldest_product - today_parse < difference_product:
                difference_product = oldest_product - today_parse
                old_date = each_product['data_de_validade']
            if today_parse - oldest_manufacture > difference_manufacture:
                difference_manufacture = today_parse - oldest_manufacture
                old_manufacture = each_product['data_de_fabricacao']
            index += 1
        return print(
                        f"Data de fabricação mais antiga: {old_manufacture} \n"
                        f"Data de validade mais próxima: {old_date}\n"
                        f"{phrase3}: {company_name_max}"
                    )
