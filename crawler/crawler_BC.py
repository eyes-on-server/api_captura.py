import requests
import pandas as pd
import pprint
from datetime import date


def start_crawler():

    data_atual = str(date.today()).replace('-', '')
    ano_mes = data_atual[:6]

    link = f"https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase=@DataBase)?@DataBase='${ano_mes}'&$top=10000&$format=json&$select=AnoMes,Municipio,Estado,Regiao,QT_PagadorPF,QT_PagadorPJ,QT_RecebedorPF,QT_RecebedorPJ"

    path_raw = fr"C:\Users\davih\OneDrive\Documentos\Faculdade\Projeto_Eyes_On_Server\api_captura.py\analytics\raw\raw{data_atual}.csv"
    path_trusted = fr"C:\Users\davih\OneDrive\Documentos\Faculdade\Projeto_Eyes_On_Server\api_captura.py\analytics\trusted\trusted{data_atual}.csv"
    path_client = fr"C:\Users\davih\OneDrive\Documentos\Faculdade\Projeto_Eyes_On_Server\api_captura.py\analytics\client\client{data_atual}.R"

    formatted_path_trusted = path_trusted.replace("\\", "/")

    requisicao = requests.get(link)
    resultado = requisicao.json()
    valores = resultado["value"]

    df = pd.DataFrame(valores)

    df.to_csv(path_raw)
    df.to_csv(path_trusted)

    try:
        r_file = open(path_client, "x")
    except FileExistsError as erro:
        r_file = open(path_client, "w")

    r_file.write(f"dataset{data_atual} <- read.csv2('{formatted_path_trusted}', sep=',', header=T)"
                 f"\ndataset{data_atual}$X <- NULL"
                 f"\nView(dataset{data_atual})")
    r_file.close()


start_crawler()
