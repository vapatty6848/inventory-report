from collections.abc import Iterable
from inventory_report import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self):
        self._company_inventory = []

    def __iter__(self):
        return InventoryIterator(self._company_inventory)
