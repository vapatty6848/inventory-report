import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def read_csv(caminho):
    '''Lê um arquivo CSV o qual o caminho é passado como parâmetro'''
    with open(caminho) as file:
        relatorio_csv = csv.DictReader(file)
        return list(relatorio_csv)


class Inventory:
    @classmethod
    def import_data(self, caminho, tipo_de_relatorio):
        '''Gera um relatorio a partir de um arquivo'''
        relatorio = read_csv(caminho)
        if tipo_de_relatorio == "simples":
            meu_relatorio = SimpleReport.generate(relatorio)
        elif tipo_de_relatorio == "completo":
            meu_relatorio = CompleteReport.generate(relatorio)
        else:
            meu_relatorio = ""
        return meu_relatorio
