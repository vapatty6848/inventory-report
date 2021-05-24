import time


my_products = [
  {
    "id": "1",
    "nome_do_produto": "Nicotine Polacrilex",
    "nome_da_empresa": "Target Corporation",
    "data_de_fabricacao": "2020-02-18",
    "data_de_validade": "2022-09-17",
    "numero_de_serie": "CR25 1551 4467 2549 4402 1",
    "instrucoes_de_armazenamento": "instrucao 1"
  },
  {
    "id": "2",
    "nome_do_produto": "fentanyl citrate",
    "nome_da_empresa": "Target Corporation",
    "data_de_fabricacao": "2019-12-06",
    "data_de_validade": "2022-12-25",
    "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
    "instrucoes_de_armazenamento": "instrucao 2"
  },
  {
    "id": "3",
    "nome_do_produto": "NITROUS OXIDE",
    "nome_da_empresa": "Galena Biopharma",
    "data_de_fabricacao": "2019-12-22",
    "data_de_validade": "2023-11-07",
    "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
    "instrucoes_de_armazenamento": "instrucao 3"
  },
  {
    "id": "4",
    "nome_do_produto": "Norepinephrine Bitartrate",
    "nome_da_empresa": "Cantrell Drug Company",
    "data_de_fabricacao": "2019-12-24",
    "data_de_validade": "2024-08-19",
    "numero_de_serie": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN",
    "instrucoes_de_armazenamento": "instrucao 4" 
  },
  {
    "id": "5",
    "nome_do_produto": "ACETAMINOPHEN, PHENYLEPHRINE HYDROCHLORIDE",
    "nome_da_empresa": "Moore Medical LLC",
    "data_de_fabricacao": "2020-04-14",
    "data_de_validade": "2024-01-14",
    "numero_de_serie": "LV23 ELDS 2GD5 X19P VCSI K",
    "instrucoes_de_armazenamento": "instrucao 5" 
  },
  {
    "id": "6",
    "nome_do_produto": "Silicea Belladonna",
    "nome_da_empresa": "Cantrell Drug Company",
    "data_de_fabricacao": "2020-07-18",
    "data_de_validade": "2023-10-05",
    "numero_de_serie": "FR57 7414 7254 046O IHVX AV6L H71",
    "instrucoes_de_armazenamento": "instrucao 6" 
  },
  {
    "id": "7",
    "nome_do_produto": "Spironolactone",
    "nome_da_empresa": "REMEDYREPACK",
    "data_de_fabricacao": "2020-07-17",
    "data_de_validade": "2022-11-18",
    "numero_de_serie": "SM28 B981 5118 903W JY0C 5KVO 3QD",
    "instrucoes_de_armazenamento": "instrucao 7" 
  },
  {
    "id": "8",
    "nome_do_produto": "Aspirin",
    "nome_da_empresa": "Galena Biopharma",
    "data_de_fabricacao": "2020-02-22",
    "data_de_validade": "2023-03-14",
    "numero_de_serie": "KZ63 800H NM4B ZOWB YYUI",
    "instrucoes_de_armazenamento": "instrucao 8" 
  },
  {
  "id": "9",
  "nome_do_produto": "eucalyptus globulus",
  "nome_da_empresa": "Target Corporation",
  "data_de_fabricacao": "2019-09-06",
  "data_de_validade": "2023-05-21",
  "numero_de_serie": "GT74 LHWJ FCXL JNQT ZCXM 4761 GWSP",
  "instrucoes_de_armazenamento": "instrucao 9"
  },
  {
    "id": "10",
    "nome_do_produto": "Titanium Dioxide",
    "nome_da_empresa": "Target Corporation",
    "data_de_fabricacao": "2019-12-08",
    "data_de_validade": "2022-12-08",
    "numero_de_serie": "FR29 5791 5333 58XR G4PR IG28 D08",
    "instrucoes_de_armazenamento": "instrucao 10"
  }
]


class SimpleReport:
    def generate(products):
        current_time = time.strftime('%Y-%m-%d')

        manufacturing_date = current_time
        expiring_date = '4000-01-01'
        biggest_number = 0
        biggest_stock_company = ''

        for date in products:
            if (date['data_de_fabricacao'] < manufacturing_date):
                manufacturing_date = date['data_de_fabricacao']
            if (date['data_de_validade'] > current_time):
                # expiring_date = date['data_de_validade']
                if date['data_de_validade'] < expiring_date:
                    expiring_date = date['data_de_validade']
            
            # Lógica de pegar a empresa que aparece mais encontrada em:
            # https://stackoverflow.com/questions/41658185/python-list-of-dictionaries-count-elements-based-on-key-of-dictionary
            number = len([d for d in products if d.get('nome_da_empresa') == date['nome_da_empresa']])
            if (number > biggest_number):
                biggest_number = number
                biggest_stock_company = date['nome_da_empresa']
        
        response = f'Data de fabricação mais antiga: {manufacturing_date}\nData de validade mais próxima: {expiring_date}\nEmpresa com maior quantidade de produtos estocados: {biggest_stock_company}\n'
        
        print(response)
        return response


SimpleReport.generate(my_products)
