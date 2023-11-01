import requests
import pandas as pd
from datetime import date
import os


def start_crawler():

    data_atual = str(date.today()).replace('-', '')
    ano_mes = data_atual[:6]

    abs_path = os.path.abspath(__file__)[:os.path.abspath(__file__).find("crawler")]

    link = (f"https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio("
            f"DataBase=@DataBase)?@DataBase='${ano_mes}'&$top=10000&$format=json&$select=AnoMes,Municipio,Estado,"
            f"Regiao,QT_PagadorPF,QT_PagadorPJ,QT_RecebedorPF,QT_RecebedorPJ")

    path_raw = abs_path + fr"analytics\raw\raw{data_atual}.csv"
    path_trusted = abs_path + fr"analytics\trusted\trusted{data_atual}.csv"
    path_client = abs_path + fr"analytics\client\client{data_atual}.R"

    formatted_path_trusted = path_trusted.replace("\\", "/")

    requisicao = requests.get(link)
    valores = requisicao.json()["value"]

    df = pd.DataFrame(valores)

    df.to_csv(path_raw)
    df.to_csv(path_trusted)

    try:
        r_file = open(path_client, "x")
    except FileExistsError:
        r_file = open(path_client, "w")

    r_file.write(f"dataset{data_atual} <- read.csv2('{formatted_path_trusted}', sep=',', header=T)"
                 f"\ndataset{data_atual}$X <- NULL"
                 f"\nView(dataset{data_atual})")
    r_file.close()


start_crawler()
