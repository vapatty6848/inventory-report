from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        extension = path.split('.')[-1]
        if (extension != 'json'):
            raise ValueError('Arquivo inválido')
        with open(path, 'r') as file:
            read = file.read()
            json_list = json.loads(read)
        return json_list
