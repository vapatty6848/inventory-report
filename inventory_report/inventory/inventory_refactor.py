from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(InventoryIterator):
    def __init__(self, importer):
        self.importer = importer
        self.data = []


    def import_data(self, file_path, import_type):
        new_data = self.importer.import_data(file_path)
        self.data = [*self.data, *new_data]

