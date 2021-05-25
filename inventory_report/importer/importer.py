from abc import ABC, abstractmethod


# requisito 6
class Importer(ABC):
    @abstractmethod
    def import_data(self, file):
        pass
