from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(self, stock):
        today = datetime.now()
        build_list = []
        validate_list = []
        name_list = []

        for item in stock:
            build_list.append(item['data_de_fabricacao'])
            validate_list.append(item['data_de_validade'])
            name_list.append(item['nome_da_empresa'])

        build = min(build_list)
        validate = min(date for date in validate_list if date > str(today))
        counter = 0
        index_list = 0
        for name in name_list:
            if name_list.count(name) > counter:
                counter = name_list.count(name)
                index_list = name_list.index(name)

        older = f'Data de fabricação mais antiga: {build}\n'
        newer = f'Data de validade mais próxima: {validate}\n'
        company = 'Empresa com maior quantidade de produtos estocados: '

        return f'{older}{newer}{company}{name_list[index_list]}\n'
