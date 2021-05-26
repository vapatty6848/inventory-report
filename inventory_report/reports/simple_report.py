from collections import Counter
from datetime import datetime


class SimpleReport:
        

    def oldest_date(products_list):
        manufacturing_date = []
        for product in products_list:
            manufacturing_date.append(product["data_de_fabricacao"])
            manufacturing_date.sort()
        old_date = manufacturing_date[0]
        return old_date

    def nearest_expiration(products_list):
        expiration_date = []
        today = '2021-05-25'
        formated_date = datetime.strptime(today, '%Y-%m-%d')
        for product in products_list:
            expiration_date.append(product["data_de_validade"])
            expiration_date.sort()
        for date in expiration_date:
            if date < today:
                expiration_date.remove(date)
        nearest_date = min(
            expiration_date, key=lambda x: abs(
                datetime.strptime(x, '%Y-%m-%d') - formated_date
            )
        )
        return nearest_date

    def repeated_company(products_list):
        company = []
        for product in products_list:
            company.append(product["nome_da_empresa"])
        occurrences = Counter(company)
        most_repeated = occurrences.most_common(1)[0][0]
        return most_repeated

  @staticmethod
  def generateReport(products_list):
      oldest = SimpleReport.oldest_date(products_list)
      nearest = SimpleReport.nearest_expiration(products_list)
      repeated = SimpleReport.repeated_company(products_list)
      return (
          f"Data de fabricação mais antiga: {oldest}\n"
          f"Data de validade mais próxima: {nearest}\n"
          f"Empresa com maior quantidade de produtos estocados: "
          f"{repeated}\n"
      )
