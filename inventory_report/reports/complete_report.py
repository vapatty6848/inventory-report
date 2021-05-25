from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(list_data):
        result = ""
        company_list = [info["nome_da_empresa"] for info in list_data]
        counter_list = Counter(company_list)
        for info in counter_list:
            result += "- %s: %s\n" % (info, counter_list[info])
        return (
            "%s\n"
            "Produtos estocados por empresa: \n"
            "%s"
            % (SimpleReport.generate(list_data), result)
        )
