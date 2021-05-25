from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(export_file):
        raise NotImplementedError
