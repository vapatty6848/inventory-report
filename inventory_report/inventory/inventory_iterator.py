from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0

    def __next__(self):
        try:
            current_value = self._iterable[self._index]
        except IndexError:
            raise StopIteration()
        else:
            self._index += 1
            return current_value

    def generate(self):
        return "vai retornar o relatório formatado como uma string"
