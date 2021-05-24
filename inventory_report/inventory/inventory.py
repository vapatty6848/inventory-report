import csv
import json
from xml.etree import ElementTree
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def read_csv(path):
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def read_json(path):
    with open(path) as file:
        data = json.load(file)

    return data


def read_xml(path):
    tree = ElementTree.parse(path)
    listOfId = tree.findall(".//id")
    listOfNomeProduto = tree.findall(".//nome_do_produto")
    listOfNomeEmpresa = tree.findall(".//nome_da_empresa")
    listOfFabricacao = tree.findall(".//data_de_fabricacao")
    listOfValidade = tree.findall(".//data_de_validade")
    listOfNumeroSerie = tree.findall(".//numero_de_serie")
    listOfInstrucoes = tree.findall(".//instrucoes_de_armazenamento")

    myList = []
    for i in range(0, len(listOfId)):
        obj = {
            "id": listOfId[i],
            "nome_do_produto": listOfNomeProduto[i].text,
            "nome_da_empresa": listOfNomeEmpresa[i].text,
            "data_de_fabricacao": listOfFabricacao[i].text,
            "data_de_validade": listOfValidade[i].text,
            "numero_de_serie": listOfNumeroSerie[i].text,
            "instrucoes_de_armazenamento": listOfInstrucoes[i].text,
        }

        myList = [*myList, obj]

    return myList


class Inventory:
    @classmethod
    def import_data(self, path, type):
        is_csv = path.endswith(".csv")
        is_json = path.endswith(".json")
        is_xml = path.endswith(".xml")

        if is_csv:
            preparedList = read_csv(path)
        if is_json:
            preparedList = read_json(path)
        if is_xml:
            preparedList = read_xml(path)

        if type == "simples":
            return SimpleReport.generate(preparedList)
        else:
            return CompleteReport.generate(preparedList)
