from inventory_report.importer.importer import Impoter
import xml.etree.ElementTree as ET


class XmlImporter(Impoter):
    def __init__(self, path):
        self.path = path

    def data_import(self):
        tree = ET.parse(self.path)
        root = tree.getroot()
        listOfdicts = []
        for record in root:
            id = record.find('id').text
            nome_do_produto = record.find('nome_do_produto').text
            nome_da_empresa = record.find('nome_da_empresa').text
            data_de_fabricacao = record.find('data_de_fabricacao').text
            data_de_validade = record.find('data_de_validade').text
            numero_de_serie = record.find('numero_de_serie').text
            instrucoes_de_armazenamento = record.find(
              'instrucoes_de_armazenamento'
            ).text
            data = {
                'id': id,
                'nome_do_produto': nome_do_produto,
                'nome_da_empresa': nome_da_empresa,
                'data_de_fabricacao': data_de_fabricacao,
                'data_de_validade': data_de_validade,
                'numero_de_serie': numero_de_serie,
                'instrucoes_de_armazenamento': instrucoes_de_armazenamento,
            }
            listOfdicts.append(data)
        return listOfdicts
