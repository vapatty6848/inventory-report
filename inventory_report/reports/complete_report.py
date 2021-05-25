from datetime import datetime


class CompleteReport:
    def __init__(self, data):
        self.data = data

    def get_company_name(all_product_list):
        get_company_names = [
            name['nome_da_empresa'] for name in all_product_list]
        company_name_max = max(get_company_names)
        return company_name_max

    def get_oldest_manufacture(all_product_list):
        date_format = "%Y-%m-%d"
        today = datetime.now().strftime(date_format)
        today_parse = datetime.strptime(today, date_format)
        index = 0
        for each_product in all_product_list:
            oldest_manu = datetime.strptime(
                each_product['data_de_fabricacao'], date_format)
            if index == 0:
                difference_manufacture = today_parse - oldest_manu
                old_manufacture = each_product['data_de_fabricacao']
            if today_parse - oldest_manu > difference_manufacture:
                difference_manufacture = today_parse - oldest_manu
                old_manufacture = each_product['data_de_fabricacao']
            index += 1
        return old_manufacture

    def oldest_product(all_product_list):
        date_format = "%Y-%m-%d"
        today = datetime.now().strftime(date_format)
        today_parse = datetime.strptime(today, date_format)
        index = 0
        for each_product in all_product_list:
            oldest_product = datetime.strptime(
                each_product['data_de_validade'], date_format)
            if index == 0 and oldest_product > today_parse:
                difference_product = oldest_product - today_parse
                old_date = each_product['data_de_validade']
            if (oldest_product - today_parse < difference_product and
                    oldest_product > today_parse):
                difference_product = oldest_product - today_parse
                old_date = each_product['data_de_validade']
            index += 1
        return old_date

    def stored_product_by_company(all_product_list):
        count_product = {}
        message = ''
        get_company_names = [
            name['nome_da_empresa'] for name in all_product_list]
        for name_company in range(len(get_company_names)):
            count_product[
                get_company_names[name_company]] = get_company_names.count(
                    get_company_names[name_company])
        for msg in count_product:
            message += f"- {msg}: {count_product[msg]}\n"
        return (
            "Produtos estocados por empresa: \n"
            f"{message}"
        )

    def generate(data):
        message = (
            f"Data de fabricação mais antiga: "
            f"{CompleteReport.get_oldest_manufacture(data)}\n"
            f"Data de validade mais próxima: "
            f"{CompleteReport.oldest_product(data)}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{CompleteReport.get_company_name(data)}\n"
            "\n"
            f"{CompleteReport.stored_product_by_company(data)}"
        )
        return message


path = [
    {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-02-18",
        "data_de_validade": "2022-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1"
    },
    {
        "id": "2",
        "nome_do_produto": "fentanyl citrate",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2019-12-06",
        "data_de_validade": "2022-12-25",
        "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
        "instrucoes_de_armazenamento": "instrucao 2"
    },
    {
        "id": "3",
        "nome_do_produto": "NITROUS OXIDE",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2019-12-22",
        "data_de_validade": "2023-11-07",
        "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
        "instrucoes_de_armazenamento": "instrucao 3"
    },
    {
        "id": "4",
        "nome_do_produto": "Norepinephrine Bitartrate",
        "nome_da_empresa": "Cantrell Drug Company",
        "data_de_fabricacao": "2019-12-24",
        "data_de_validade": "2024-08-19",
        "numero_de_serie": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN",
        "instrucoes_de_armazenamento": "instrucao 4"
    },
    {
        "id": "5",
        "nome_do_produto": "ACETAMINOPHEN, PHENYLEPHRINE HYDROCHLORIDE",
        "nome_da_empresa": "Moore Medical LLC",
        "data_de_fabricacao": "2020-04-14",
        "data_de_validade": "2024-01-14",
        "numero_de_serie": "LV23 ELDS 2GD5 X19P VCSI K",
        "instrucoes_de_armazenamento": "instrucao 5"
    },
    {
        "id": "6",
        "nome_do_produto": "Silicea Belladonna",
        "nome_da_empresa": "Cantrell Drug Company",
        "data_de_fabricacao": "2020-07-18",
        "data_de_validade": "2023-10-05",
        "numero_de_serie": "FR57 7414 7254 046O IHVX AV6L H71",
        "instrucoes_de_armazenamento": "instrucao 6"
    },
    {
        "id": "7",
        "nome_do_produto": "Spironolactone",
        "nome_da_empresa": "REMEDYREPACK",
        "data_de_fabricacao": "2020-07-17",
        "data_de_validade": "2022-11-18",
        "numero_de_serie": "SM28 B981 5118 903W JY0C 5KVO 3QD",
        "instrucoes_de_armazenamento": "instrucao 7"
    },
    {
        "id": "8",
        "nome_do_produto": "Aspirin",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2020-02-22",
        "data_de_validade": "2023-03-14",
        "numero_de_serie": "KZ63 800H NM4B ZOWB YYUI",
        "instrucoes_de_armazenamento": "instrucao 8"
    },
    {
        "id": "9",
        "nome_do_produto": "eucalyptus globulus",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2019-09-06",
        "data_de_validade": "2023-05-21",
        "numero_de_serie": "GT74 LHWJ FCXL JNQT ZCXM 4761 GWSP",
        "instrucoes_de_armazenamento": "instrucao 9"
    },
    {
        "id": "10",
        "nome_do_produto": "Titanium Dioxide",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2019-12-08",
        "data_de_validade": "2022-12-08",
        "numero_de_serie": "FR29 5791 5333 58XR G4PR IG28 D08",
        "instrucoes_de_armazenamento": "instrucao 10"
    }
]
message = CompleteReport.generate(path)
print(message)
