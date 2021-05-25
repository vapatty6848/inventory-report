import json
from abc import abstractmethod
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @abstractmethod
    def import_data(file_path):
        extension = file_path.split('.')[-1]
        if extension != 'json':
            raise ValueError('Arquivo inválido')

        content_list = []
        with open(file_path, newline='') as jsonfile:
            content_list = json.load(jsonfile)

        return content_list
