from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __iter__(self):
        self.product_index = 0

        return self

    def __next__(self):
        product = self.data[self.product_index]

        self.product_index += 1

        return product
