from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, data):
        conjunto_empresa_valor = []

        for product in data:
            for dict_empresa in conjunto_empresa_valor:
                if product["nome_da_empresa"] == dict_empresa["empresa"]:
                    dict_empresa["estoque"] += 1
                    break
            else:
                conjunto_empresa_valor.append({
                    "empresa": product["nome_da_empresa"],
                    "estoque": 1
                })

        string = "\nProdutos estocados por empresa: \n"
        for empresa_estoque in conjunto_empresa_valor:
            empresa = empresa_estoque["empresa"]
            estoque = empresa_estoque["estoque"]
            string += f"- {empresa}: " + f"{estoque}\n"

        return super().generate(data) + string
