from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(list_data):
        company_list = []
        result = ""
        for company in list_data:
            company_list.append(company["nome_da_empresa"])
        test = Counter(company_list)
        for info in test:
            result += "- %s: %s\n" % (info, test[info])
        return (
            "%s\n"
            "Produtos estocados por empresa: \n"
            "%s"
            % (SimpleReport.generate(list_data), result)
        )
