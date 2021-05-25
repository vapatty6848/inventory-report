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
    @classmethod
    def maxDate(cls, dict_key, date_list):
        cls.dict_key = dict_key
        cls.date_list = date_list

        list = [date[cls.dict_key] for date in cls.date_list]
        max_date = datetime.date(
            max([datetime.strptime(date, "%Y-%m-%d") for date in list])
        )
        result = datetime.strftime(max_date, "%Y-%m-%d")
        return result

    @classmethod
    def minDate(cls, dict_key, date_list):
        cls.dict_key = dict_key
        cls.date_list = date_list

        list = [date[cls.dict_key] for date in cls.date_list]
        min_date = datetime.date(
            min([datetime.strptime(date, "%Y-%m-%d") for date in list])
        )
        result = datetime.strftime(min_date, "%Y-%m-%d")
        return result

    @classmethod
    def closestDateFromNow(cls, dict_key, date_list):
        cls.dict_key = dict_key
        cls.date_list = date_list
        now = str(datetime.now())

        list = [
            date[cls.dict_key]
            for date in cls.date_list
            if date[cls.dict_key] > now
        ]
        result = min(list)
        return result


class SimpleReport:
    @classmethod
    def generate(cls, document):
        cls.document = document
        companies_list = [item["nome_da_empresa"] for item in cls.document]

        oldest_fab_date = DateHandler.minDate(
          "data_de_fabricacao",
          cls.document
        )

        closest_expire_date = DateHandler.closestDateFromNow(
            "data_de_validade",
            cls.document
        )
        lrgst_storage = mode(companies_list)

        result = (
"""Data de fabricação mais antiga: {}
Data de validade mais próxima: {}
Empresa com maior quantidade de produtos estocados: {}
""".format(oldest_fab_date, closest_expire_date, lrgst_storage))

        return result


report = SimpleReport.generate(list_mock)

print(report)
