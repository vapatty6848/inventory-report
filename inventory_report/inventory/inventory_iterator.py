from abc import abstractmethod
from collections.abc import Iterator


class InventoryIterator(Iterator):
    @abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @abstractmethod
    def __next__(self):
        raise NotImplementedError
