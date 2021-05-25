from inventory_report.importer.importer import Importer
import xmltodict
import json


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        file_type = path.split(".")[-1]
        if file_type != "xml":
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            xpars = xmltodict.parse(file.read())
        res_json = json.dumps(xpars)
        return json.loads(res_json)["dataset"]["record"]
