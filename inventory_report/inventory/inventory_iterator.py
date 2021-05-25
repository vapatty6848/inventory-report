from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterable):
        self._iterable = iterable
        self._position = 0

    def __next__(self):
        """Retorna o próximo elemento da coleção.
        Uma exceção é lançada quando não há mais elementos a serem percorridos.
        """
        try:
            current_value = self._iterable[self._position]
        except IndexError:
            raise StopIteration()
        else:
            self._position += 1
            return current_value
