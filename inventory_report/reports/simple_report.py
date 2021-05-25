# Adicionando alteração e seja o que deus quiser!
from datetime import datetime
from statistics import mode

list_mock = [
  {
    "id": 1,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
    {
    "id": 2,
    "nome_do_produto": "GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "PRODAP",
    "data_de_fabricacao": "2020-05-04",
    "data_de_validade": "2022-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 082",
    "instrucoes_de_armazenamento": "um mauris non ligula pellentesque ultrices    phasellus"
  },
  {
    "id": 3,
    "nome_do_produto": "GERANIUM MACULATUM ROOT, SODIUM CHLORIDE ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "PRODAP",
    "data_de_fabricacao": "2015-05-04",
    "data_de_validade": "2022-03-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "um mauris non ligula pellentesque ultrices"
  }
]


class DateHandler:
    def __init__(self, date_list):
        self.date_list = date_list

    def maxDate(self, dict_key):
        self.dict_key = dict_key
        list = [date[self.dict_key] for date in self.date_list]
        max_date = datetime.date(
            max([datetime.strptime(date, "%Y-%m-%d") for date in list])
        )
        result = datetime.strftime(max_date, "%Y-%m-%d")
        return result

    def minDate(self, dict_key):
        self.dict_key = dict_key
        list = [date[self.dict_key] for date in self.date_list]
        min_date = datetime.date(
            min([datetime.strptime(date, "%Y-%m-%d") for date in list])
        )
        result = datetime.strftime(min_date, "%Y-%m-%d")
        return result


class SimpleReport:
    def __init__(self, document):
        self.document = document

    def generate(self):
        date_class = DateHandler(self.document)
        companies_list = [item["nome_da_empresa"] for item in self.document]

        oldest_fab_date = date_class.minDate("data_de_fabricacao")
        closest_expire_date = date_class.minDate("data_de_validade")
        lrgst_storage = mode(companies_list)

        return ({
          "Data de fabricação mais antiga": oldest_fab_date,
          "Data de validade mais próxima": closest_expire_date,
          "Empresa com maior quantidade de produtos estocados": lrgst_storage,
        })


new_report = SimpleReport(list_mock)

print(new_report.generate())
