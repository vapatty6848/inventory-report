from inventory_report.importer.importer import Importer
import json


def read_json(path):
    with open(path) as file:
        data = json.load(file)

    return data


class JsonImporter(Importer):
    @classmethod
    def import_data(self, file):
        is_json = file.endswith(".json")

        if not is_json:
            raise ValueError("Arquivo inválido")

        preparedList = read_json(file)
        return preparedList
