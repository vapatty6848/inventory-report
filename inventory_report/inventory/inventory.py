import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def read_csv(caminho):
    '''Lê um arquivo CSV o qual o caminho é passado como parâmetro'''
    with open(caminho) as file:
        relatorio_csv = csv.DictReader(file)
        return list(relatorio_csv)


def read_json(caminho):
    '''Lê um arquivo JSON o qual o caminho é passado como parâmetro'''
    with open(caminho) as file:
        return json.load(file)


def choose_reader(caminho):
    '''Verifica qual a extensão do arquivo antes de ler o relatório'''
    if caminho.endswith(".csv"):
        return read_csv(caminho)
    elif caminho.endswith(".json"):
        return read_json(caminho)
    else:
        return False


class Inventory:
    @classmethod
    def import_data(self, caminho, tipo_de_relatorio):
        '''Gera um relatorio a partir de um arquivo'''
        relatorio = choose_reader(caminho)
        if relatorio is not False:
            if tipo_de_relatorio == "simples":
                meu_relatorio = SimpleReport.generate(relatorio)
            elif tipo_de_relatorio == "completo":
                meu_relatorio = CompleteReport.generate(relatorio)
            else:
                meu_relatorio = "Falha ao gerar"
            return meu_relatorio
        else:
            return "Algo deu errado"
