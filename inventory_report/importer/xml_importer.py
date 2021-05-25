from inventory_report.importer.importer import Importer
from xml.etree import ElementTree


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
            "id": listOfId[i].text,
            "nome_do_produto": listOfNomeProduto[i].text,
            "nome_da_empresa": listOfNomeEmpresa[i].text,
            "data_de_fabricacao": listOfFabricacao[i].text,
            "data_de_validade": listOfValidade[i].text,
            "numero_de_serie": listOfNumeroSerie[i].text,
            "instrucoes_de_armazenamento": listOfInstrucoes[i].text,
        }

        myList = [*myList, obj]

    return myList


class XmlImporter(Importer):
    @classmethod
    def import_data(self, file):
        is_xml = file.endswith(".xml")

        if not is_xml:
            raise ValueError("Arquivo inválido")

        preparedList = read_xml(file)
        return preparedList
