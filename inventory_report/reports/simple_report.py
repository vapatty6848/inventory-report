from collections import Counter
from datetime import datetime


class SimpleReport:
    """Gera um relatório com os dados advindos do data"""
    @classmethod
    def generate(cls, data):
        """Busca a empresa que mais vezes aparece,"""
        """ ou seja, com mais produtos"""
        list_name_companies = [
            data_report["nome_da_empresa"] for data_report in data
        ]
        companies_counter = Counter(list_name_companies)
        company_max_shows = max(companies_counter)

        """Busca a data de fabricação de menor valor"""
        list_date_fabricate = [
            data_report["data_de_fabricacao"] for data_report in data
        ]
        date_fabricate_min = min(list_date_fabricate)

        """Busca a data de validade de menor valor"""
        today_date = str(datetime.now())
        list_date_valid = [
            data_report["data_de_validade"]
            for data_report in data
            if data_report["data_de_validade"] >= today_date
        ]
        date_valid_min = min(list_date_valid)

        return (
            f'Data de fabricação mais antiga: {date_fabricate_min}\n'
            + f'Data de validade mais próxima: {date_valid_min}\n'
            + 'Empresa com maior quantidade de produtos estocados: '
            + f'{company_max_shows}\n'
        )
