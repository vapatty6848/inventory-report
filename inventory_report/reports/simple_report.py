from datetime import datetime
from typing import Counter


# dict_list = [
#     {
#         "id": 1,
#         "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2020-07-04",
#         "data_de_validade": "2023-02-09",
#         "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#         "instrucoes_de_armazenamento": "in blandit ultrices enim",
#     },
#     {
#         "id": 2,
#         "nome_do_produto": "sodium ferric gluconate complex",
#         "nome_da_empresa": "sanofi-aventis U.S. LLC",
#         "data_de_fabricacao": "2020-05-31",
#         "data_de_validade": "2023-01-17",
#         "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
#         "instrucoes_de_armazenamento": "duis bibendum morbi",
#     },
#     {
#         "id": 3,
#         "nome_do_produto": "Dexamethasone Sodium Phosphate",
#         "nome_da_empresa": "sanofi-aventis U.S. LLC",
#         "data_de_fabricacao": "2019-09-13",
#         "data_de_validade": "2023-02-13",
#         "numero_de_serie": "BA52 2034 8595 7904 7131",
#         "instrucoes_de_armazenamento": "morbi quis tortor id",
#     },
#     {
#         "id": 4,
#         "nome_do_produto": "Uricum acidum, Benzoicum acidum",
#         "nome_da_empresa": "Newton Laboratories, Inc.",
#         "data_de_fabricacao": "2019-11-08",
#         "data_de_validade": "2019-11-25",
#         "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
#         "instrucoes_de_armazenamento": "velit eu est congue elementum",
#     },
# ]


class SimpleReport:
    def generate(generalList):
        dateManufacturing = []
        dateValidation = []
        companyNames = []
        for item in generalList:
            dateManufacturing.append(item["data_de_fabricacao"])
            dateValidation.append(item["data_de_validade"])
            companyNames.append(item["nome_da_empresa"])
        # print(companyNames)
        dateManufacturing.sort(
            key=lambda date: datetime.strptime(date, "%Y-%m-%d")
        )
        dateValidation.sort(
            key=lambda date: datetime.strptime(date, "%Y-%m-%d")
        )
        currentYear = str(datetime.now())[0:4]
        newDateValidation = []
        for date in dateValidation:
            if date[0:4] > currentYear:
                newDateValidation.append(date)
        companies = Counter(companyNames)
        company = companies.most_common()[0][0].strip()
        dateManufacturingOld = dateManufacturing[0].strip()
        dateNextValidate = newDateValidation[0].strip()
        facOld = f"Data de fabricação mais antiga: {dateManufacturingOld}\n"
        nextValidate = f"Data de validade mais próxima: {dateNextValidate}\n"
        c = f"Empresa com maior quantidade de produtos estocados: {company}\n"
        print(newDateValidation)
        result = f"{facOld}{nextValidate}{c}"

        return result


# SimpleReport.generate(dict_list)
