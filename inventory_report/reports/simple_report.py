import datetime
class SimpleReport:
    def generate(listOfdicts=[]):
        madeIn = None
        usableTill = None
        companyName = ''
        companies = [item['nome_da_empresa'] for item in listOfdicts]
        companyCount = 0
        
        for item in listOfdicts:
            if madeIn is None:
                madeIn = datetime.date.fromisoformat(item['data_de_fabricacao'])
            else:
                if madeIn > datetime.date.fromisoformat(item['data_de_fabricacao']):
                    madeIn = datetime.date.fromisoformat(item['data_de_fabricacao'])
            if usableTill is None:
                if datetime.date.fromisoformat(item['data_de_validade']) >= datetime.date.today():
                    usableTill = datetime.date.fromisoformat(item['data_de_validade'])
            else:
                if usableTill > datetime.date.fromisoformat(item['data_de_validade']) and datetime.date.fromisoformat(item['data_de_validade']) >= datetime.date.today():
                    usableTill = datetime.date.fromisoformat(item['data_de_validade'])

        for company in companies:
            if companyCount < companies.count(company):
                companyCount = companies.count(company)
                companyName = company

        formattedData1 = f"Data de fabricação mais antiga: {madeIn.isoformat()}"
        formattedData2 = f"Data de validade mais próxima: {usableTill.isoformat()}"
        formattedData3 = f"Empresa com maior quantidade de produtos estocados: {companyName}"
        formattedData = '\n'.join([formattedData1, formattedData2, formattedData3])
        print(formattedData)

        