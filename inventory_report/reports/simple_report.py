import datetime


class SimpleReport:
    def __init__(self, listOfdicts=[]):
        self.listOfdicts = listOfdicts

    def _getLargestStock(self):
        companyName = ''
        companyCount = 0
        companies = [item['nome_da_empresa'] for item in self.listOfdicts]
        for company in companies:
            if companyCount < companies.count(company):
                companyCount = companies.count(company)
                companyName = company
        return companyName

    def _getMadeIn(self):
        madeIn = datetime.date(datetime.MAXYEAR, 12, 31)
        for item in self.listOfdicts:
            if madeIn > datetime.date.fromisoformat(
                item['data_de_fabricacao']
            ):
                madeIn = datetime.date.fromisoformat(
                    item['data_de_fabricacao']
                )
        return madeIn.isoformat()

    def _getUsableTill(self):
        today = datetime.date.today()
        usableTill = datetime.date(datetime.MAXYEAR, 12, 31)
        for item in self.listOfdicts:
            currentDate = datetime.date.fromisoformat(item['data_de_validade'])
            if usableTill > currentDate and currentDate >= today:
                usableTill = currentDate
        return usableTill.isoformat()

    def generate(self):
        formattedData1 = f"Data de fabricação mais antiga: {self._getMadeIn()}"
        formattedData2 = f"Data de validade mais próxima: {self._getUsableTill()}"
        formattedData3 = f"Empresa com maior quantidade de produtos estocados: {self._getLargestStock()}"
        formattedData = '\n'.join([formattedData1, formattedData2, formattedData3])
        print(formattedData)

        