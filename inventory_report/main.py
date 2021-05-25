from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)
    else:
        _, file_path, report_type = sys.argv
        if file_path.endswith('.csv'):
            instance = InventoryRefactor(CsvImporter)
        if file_path.endswith('.json'):
            instance = InventoryRefactor(JsonImporter)
        if file_path.endswith('.xml'):
            instance = InventoryRefactor(XmlImporter)
        report = instance.import_data(file_path, report_type)
        print(report, end="")
