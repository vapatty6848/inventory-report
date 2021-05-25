from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


def parse_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()

    records = root.findall('record')

    items = []

    for record in records:
        item_dict = {}

        for node in record.iter():
            item_dict[node.tag] = node.text

        items.append(item_dict)

    return items


def get_file_extension(file_path):
    file_pieces = file_path.split('.')
    file_pieces.reverse()

    file_extension = file_pieces[0]

    return file_extension


extension_to_reader = {
    'json': json.load,
    'csv': csv.DictReader,
    'xml': parse_xml,
}

class Inventory:

    @staticmethod
    def import_data(file_path, method):
        products = []

        with open(file_path) as csvfile:
            extension = get_file_extension(file_path)
            reader = extension_to_reader[extension]

            products = list(reader(csvfile))

            simple_method = method == 'simples'
            Reporter = SimpleReport if simple_method else CompleteReport

            answer = Reporter.generate(products)

            return answer


