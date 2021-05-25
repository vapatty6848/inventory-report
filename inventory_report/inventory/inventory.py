import csv
import json
from xml_to_dict import XMLtoDict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, tipoRelatorio):

        if path.split(".", 1)[1] == "csv":
            relatorio = Inventory.leitor_csv(path)
        if path.split(".", 1)[1] == "json":
            relatorio = Inventory.leitor_json(path)
        if path.split(".", 1)[1] == "xml":
            relatorio = Inventory.leitor_xml(path)

        if tipoRelatorio == "simples":
            return SimpleReport.generate(relatorio)
        else:
            return CompleteReport.generate(relatorio)

    def leitor_csv(path):
        lista_produtos = []
        with open(path, newline="") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                lista_produtos.append(row)
        return lista_produtos

    def leitor_json(path):
        with open(path) as file:
            content = json.load(file)
            return content

    def leitor_xml(path):
        with open(path) as file:
            parser = XMLtoDict()
            xml_file = file.read()
            content = parser.value_from_nest("record", xml_file)
            return content
