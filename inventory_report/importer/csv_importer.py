from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        extension = path.split('.')[-1]
        if (extension != 'csv'):
            raise ValueError('Arquivo inválido')
        with open(path, 'r') as file:
            mycsv = csv.DictReader(file, delimiter=",")
            csv_list = []
            for row in mycsv:
                csv_list.append(row)
        return csv_list
