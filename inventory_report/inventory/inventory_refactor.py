from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(InventoryIterator):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        self.data = [*self.data, *self.importer.import_data(path)]

    def __iter__(self):
        return iter(self.data)

    def __next__(self, iterator):
        return next(iterator)
