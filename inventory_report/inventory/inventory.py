import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def open_csv(path):
        inventory_data = []
        with open(path) as csv_file:
            inventory_data_csv = csv.DictReader(csv_file)
            [inventory_data.append(row) for row in inventory_data_csv]
        return inventory_data

    @staticmethod
    def open_json(path):
        with open(path) as json_file:
            inventory_data_json = json.load(json_file)
        return inventory_data_json

    @staticmethod
    def open_xml(path):
        inventory_data = []
        with open(path) as xml_file:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            all_records = root.findall('record')
            for item in all_records:
                inventory = {element.tag: element.text for element in item}
                inventory_data.append(inventory)
        return inventory_data

    @staticmethod
    def import_data(path, version):
        if path.endswith(".csv"):
            list_inventory = Inventory.open_csv(path)
        elif path.endswith(".json"):
            list_inventory = Inventory.open_json(path)
        else:
            list_inventory = Inventory.open_xml(path)

        report = (
            CompleteReport.generate(list_inventory)
            if version == "completo"
            else SimpleReport.generate(list_inventory)
        )
        return report


results = Inventory()
list_inventory = results.import_data(
    'inventory_report/data/inventory.xml', "completo"
)
print(list_inventory)
