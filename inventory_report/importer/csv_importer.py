from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        file_type = path.split(".")[-1]
        if file_type != "csv":
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            status_reader = csv.reader(file, delimiter=",", quotechar='"')
            headers, *data = status_reader
        array = []
        for values in data:
            obj = {}
            for index, header in enumerate(headers):
                obj[header] = values[index]
            array.append(obj)
        return array
