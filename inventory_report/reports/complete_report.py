from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def get_stock_by_company(self, data):
        """Gera relatório de produtos por companias"""
        list_name_companies = [
            data_report["nome_da_empresa"] for data_report in data
        ]
        companies_number_product_dictionary = Counter(list_name_companies)
        companies_number_array_tuplas = (
            companies_number_product_dictionary.items()
        )
        string_base = "\nProdutos estocados por empresa: \n"
        for t in companies_number_array_tuplas:
            index_tuplas = f"- {t[0]}: {t[1]}\n"
            string_base += index_tuplas
        return string_base

    @classmethod
    def generate(cls, data):
        """Gera relatório de produtos por companias"""
        simple_generate = super().generate(data)
        stock_by_company = CompleteReport.get_stock_by_company(data)
        return simple_generate + stock_by_company
