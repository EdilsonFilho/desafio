import csv
import requests
import psycopg2
import json
from psycopg2 import Error
from pprint import pprint
from sqlalchemy.sql import func




#app =Flask(__name__)
#app.config['DEBUG']= True
#db = SQLAlchemy()
print('########################################')
print('#   CONSULTA USANDO API E POSTGRES     #')
print('#    VISAO GERAL DA PESQUISA           #')
print('# 10 COMPRAS REALIZADAS SEM LICITACAO  #')
print('#          ANO DE 2019                 #')
print('########################################')
con = psycopg2.connect(
        user = "postgres",
        password = "aryanalinda",
        host = "localhost",
        port = "5432",
        dbname = "postgres")
print("!!SUCESSO NA CONEXÃO COM BD!!")
print("\n\n")

def main():
    
    option = int(input('Qual consulta desejas realizar?\n 1.Maior valor de licitacao\n 2.Menor valor de licitacao\n 3.Soma total do valor usado sem licitacao em 2019\n 4.Média do valor usado sem licitacao em 2019\n 5. Informações gerais\n 6.Sair\n'))

    cursor = con.cursor()
    cursor.execute("select valor,itens,fornecedor,quantidade, n_servico,materiais_contratados from compras_slicitacao;")
    rows = cursor.fetchall()
    s = 0
    6
    maior=0
    menor=0
    #optcao de consulta para maior e menor
    for c in rows:
        aux =  c[0]
        if maior < aux:
            maior = aux
            aux=0
        elif maior > aux:
            menor = aux
    #optcao de consulta para soma e media
    for c in rows:
        n = c[0]
        s += n

    if option == 1:
      print('Valor maior é R$ {:.2f}\n'.format(maior))
      option = 7
    if option == 2:
      print('Valor menor é R$ {:.2f}\n'.format(menor))
      option = 7
    if option == 3:
     print('Somatório dos valores: R$ {}\n'.format(s))
     option = 7
    if option == 4:
        print('Valor médio das compras: R$ {:.2f}\n'.format(s/10))
        option = 7

    if option == 5:
        for r in rows:
        
            print(f"valor R$ {r[0]} e o link do iten está em: {r[1]}")
            print(f"O fornecedor é: {r[2]}, a quantidade é : {r[3]}")
            print(f"O número de serviço é : {r[4]}, e o material contratado é : {r[5]}")
            print('--------------------------------------------------------------------\n')
            option = 7
    if option == 6:
        print('SAINDO DA APLICAÇÃO')
        print('-------------------')
    if option == 7:
        main()
   

    '''
    for r in rows:
        print(f"valor R$ {r[0]} e o descritivo do iten está em: {r[1]}")
        request = requests.get('http://compras.dados.gov.br{}.json'.format(r[1]))
        #print(request)
        # requ = requests.get('http://compras.dados.gov.br/compraSemLicitacao/doc/item_slicitacao/15871907000012019/itens.json')
        tit = json.loads(request.text)
        print('---Mostrando ITENS-----')
        print(tit['_embedded']['compras'][0]['ds_detalhada'])
        print('--- FIM DE Mostrando ITENS-----')
        print('#*#*#*#*#*#*#*#')
        print('---Mostrando VALOR-----')
        print('o valor do contrato foi  de R$ {}'.format(tit['_embedded']['compras'][0]['vr_estimado']))
        print('--- FIM DE Mostrando VALOR-----')
        print('#*#*#*#*#*#*#*#')
        print('---Mostrando FORNECEDOR-----')
        print(tit['_embedded']['compras'][0]['_links']['self'])
        print('--- FIM DE Mostrando FORNECEDOR-----')
    '''
     
    
    
    con.close()
    
    

if __name__ == '__main__':
    main()