import csv
import requests




#app =Flask(__name__)
#app.config['DEBUG']= True
#db = SQLAlchemy()

def main():

    print('##Consulta na API###')

    request = requests.get('http://compras.dados.gov.br/compraSemLicitacao/v1/compras_slicitacao.json?co_orgao=26233&dt_ano_aviso_licitacao=2019')

    print(request.json())

if __name__ == '__main__':
    main()