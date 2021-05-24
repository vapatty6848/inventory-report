from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(self, produtos):
        fabricacao_mais_antiga = produtos[0]["data_de_fabricacao"]
        validade_mais_proxima = produtos[0]["data_de_validade"]
        dataAtual = datetime.now().isoformat()
        empresas = []

        for produto in produtos:
            validade = produto["data_de_validade"]
            fabricacao = produto["data_de_fabricacao"]
            if validade >= dataAtual and validade < validade_mais_proxima:
                validade_mais_proxima = produto["data_de_validade"]
            if fabricacao <= dataAtual and fabricacao < fabricacao_mais_antiga:
                fabricacao_mais_antiga = produto["data_de_fabricacao"]
            empresas = [*empresas, produto["nome_da_empresa"]]

        self.labelValidade = (
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
        )
        self.labelFabricacao = (
            f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
        )
        self.labelEmpresa = f"Empresa com maior quantidade de produtos estocados: {max(empresas)}\n"

        return self.labelFabricacao + self.labelValidade + self.labelEmpresa
