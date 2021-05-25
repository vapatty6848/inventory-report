import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.utils.file_extension_parser import get_file_extension
from inventory_report.utils.parse_xml import parse_xml

extension_to_reader = {
    'json': json.load,
    'csv': csv.DictReader,
    'xml': parse_xml,
}

class Inventory:
    @staticmethod
    def import_data(file_path, method):
        products = []

        with open(file_path) as file:
            extension = get_file_extension(file_path)
            reader = extension_to_reader[extension]

            products = list(reader(file))

            simple_method = method == 'simples'
            Reporter = SimpleReport if simple_method else CompleteReport

            answer = Reporter.generate(products)

            return answer


