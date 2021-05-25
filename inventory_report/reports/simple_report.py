from statistics import mode
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(self, data):
        date_now = datetime.now()
        nomes_das_empresas = []
        datas_de_fabricacao = []
        datas_de_validade = []
        for product in data:
            nomes_das_empresas.append(product["nome_da_empresa"])
            datas_de_fabricacao.append(product["data_de_fabricacao"])
            validade = product["data_de_validade"]
            if datetime.strptime(validade, "%Y-%m-%d") >= date_now:
                datas_de_validade.append(validade)
        datas_de_fabricacao.sort(
          key=lambda date: datetime.strptime(date, "%Y-%m-%d")
        )
        datas_de_validade.sort(
          key=lambda date: datetime.strptime(date, "%Y-%m-%d")
        )
        empresa_maior_quantidade = mode(nomes_das_empresas)
        return (
            f"Data de fabricação mais antiga: {datas_de_fabricacao[0]}" +
            f"\nData de validade mais próxima: {datas_de_validade[0]}" +
            "\nEmpresa com maior quantidade de " +
            f"produtos estocados: {empresa_maior_quantidade}\n"
        )
