from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.utils import ReportsUtils


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(report_list):
        oldest = ReportsUtils.get_oldest(report_list)
        next_to_expire = ReportsUtils.get_next_to_expire(report_list)
        largest = ReportsUtils.get_largest_stock(report_list)
        stock = ReportsUtils.get_stock(report_list)
        stock_report = ""
        for key in stock:
            stock_report += f"- {key}: {stock[key]}\n"
        complete_report = (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {next_to_expire}\n"
            f"Empresa com maior quantidade de produtos estocados: {largest}\n"
            "\nProdutos estocados por empresa: \n"
            f"{stock_report}"
        )
        return complete_report
