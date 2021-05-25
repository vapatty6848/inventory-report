import sys

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.utils.file_extension_parser import get_file_extension
from inventory_report.inventory.inventory_refactor import InventoryRefactor

MINIMUM_ARG_LENGTH = 3
FIRST_ARGUMENT = 1

extension_to_importer = {
    "json": JsonImporter,
    "csv": CsvImporter,
    "xml": XmlImporter,
}


def main():
    args = sys.argv

    if len(args) < MINIMUM_ARG_LENGTH:
        return print("Verifique os argumentos", file=sys.stderr)

    [file_path, report_type] = args[FIRST_ARGUMENT:MINIMUM_ARG_LENGTH]

    extension = get_file_extension(file_path)

    importer = extension_to_importer[extension]

    Inventory = InventoryRefactor(importer)
    Inventory.import_data(file_path, report_type)

    report = Inventory.generate_report()

    print(report, end="")
