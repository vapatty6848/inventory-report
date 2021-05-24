from datetime import datetime


class SimpleReport:
    def generate(list_data):
        today = datetime.today().strftime('%Y-%m-%d')
        older = list_data[0]["data_de_fabricacao"]
        validity_list = [today]
        company_list = []
        init = 0
        for info in list_data:
            factory = info["data_de_fabricacao"]
            validity = info["data_de_validade"]
            company = info["nome_da_empresa"]
            company_list.append(company)
            validity_list.append(validity)
            if (factory < older):
                older = factory

        for names in company_list:
            count = company_list.count(names)
            if (count > init):
                init = count
                name = names

        sort = sorted(validity_list)
        index = sort.index(today)
        closest = sort[index + 1]

        return (
            "Data de fabricação mais antiga: %s\n"
            "Data de validade mais próxima: %s\n"
            "Empresa com maior quantidade de produtos estocados: %s\n"
            % (older, closest, name)
        )
