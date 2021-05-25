from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self, listOfdicts=[]):
        super().__init__(listOfdicts)

    def generate(self):
        super().generate()
        companies = [item['nome_da_empresa'] for item in self.listOfdicts]
        print('\nProdutos estocados por empresa:')
        companySet = set()
        for company in companies:
            if company not in companySet:
                print(f'- {company}: {companies.count(company)}')
                companySet.add(company)
