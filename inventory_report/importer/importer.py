from abc import ABC, abstractmethod

from inventory_report.utils.file_extension_parser import get_file_extension


class Importer(ABC):
    @staticmethod
    @abstractmethod
    def import_data(file_path):
        raise NotImplementedError

    @staticmethod
    def validate_extension(file_path, extension_wanted):
        extension = get_file_extension(file_path)

        invalid_extension = extension != extension_wanted

        if (invalid_extension):
            raise ValueError('Arquivo inválido')
