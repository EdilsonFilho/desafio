import csv
import requests
import psycopg2
import json
from psycopg2 import Error
from pprint import pprint




#app =Flask(__name__)
#app.config['DEBUG']= True
#db = SQLAlchemy()

def main():

    print('###########Consulta na API#############')
    con = psycopg2.connect(
        user = "postgres",
        password = "aryanalinda",
        host = "localhost",
        port = "5432",
        dbname = "postgres")
    print("CONEXÃO COM BD DO POSTGRESQL REALIZADA COM SUCESSO!")

    cursor = con.cursor()
    cursor.execute("select valor,itens,fornecedor,quantidade, n_servico,materiais_contratados from compras_slicitacao;")
    rows = cursor.fetchall()

    print(' VISAO GERAL DA PESQUISA')
    print(' COM 10 COMPRAS REALIZADAS SEM LICITACAO PERIODO DE 2019')
    for r in rows:
       
        print(f"valor R$ {r[0]} e o link do iten está em: {r[1]}")
        print(f"O fornecedor é: {r[2]}, a quantidade é : {r[3]}")
        print(f"O número de serviço é : {r[4]}, e o material contratado é : {r[5]}")
        print('--------------------------------------------------------------------')


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