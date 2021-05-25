import csv
from abc import abstractmethod
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @abstractmethod
    def import_data(file_path):
        extension = file_path.split('.')[-1]
        if extension != 'csv':
            raise ValueError('Arquivo inválido')
        content_list = []
        with open(file_path, newline='') as csvfile:
            content = csv.DictReader(csvfile, delimiter=",")
            for curr_dict in content:
                current = {}
                for key in curr_dict:
                    current[key] = curr_dict[key]
                content_list.append(current)

        return content_list
