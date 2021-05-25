from inventory_report.reports.simple_report import SimpleReport

class CompleteReport(SimpleReport):

    @staticmethod
    def generate(products):
        simple_report =  SimpleReport.generate(products)
        products_count = {}

        for product in products:
            company = product['nome_da_empresa']

            products_count[company] = (
                products_count[company] + 1 if company in products_count else 1
            )

        products_per_company = [f"- {company}: {count}" for (company, count) in products_count.items()]
        complete_answer = '\n'.join(['Produtos estocados por empresa: ', *products_per_company])

        return simple_report + '\n' + complete_answer + '\n'


