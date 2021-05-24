from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(listOfdicts=[]):
        SimpleReport.generate(listOfdicts)
        companies = [item['nome_da_empresa'] for item in listOfdicts]
        print('\nProdutos estocados por empresa:')
        companySet = set()
        for company in companies:
            if company not in companySet:
                print(f'- {company}: {companies.count(company)}')
                companySet.add(company)
