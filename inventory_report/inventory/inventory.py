import csv
import json
import xml.etree.ElementTree as ET
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


def read_xml(caminho):
    '''Lê um arquivo XML o qual o caminho é passado como parâmetro'''
    '''ref: datacamp;com / tutorial / Python XML with ElementTree'''
    root = ET.parse(caminho).getroot()
    relatorio = []
    for child in root:
        dict_format = {}
        for tag in child:
            # print(tag)
            # print(tag.text)
            # print(tag.tag)
            dict_format[tag.tag] = tag.text
        relatorio.append(dict_format)
    return relatorio


def choose_reader(caminho):
    '''Verifica qual a extensão do arquivo antes de ler o relatório'''
    if caminho.endswith(".csv"):
        return read_csv(caminho)
    elif caminho.endswith(".json"):
        return read_json(caminho)
    elif caminho.endswith(".xml"):
        return read_xml(caminho)
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
