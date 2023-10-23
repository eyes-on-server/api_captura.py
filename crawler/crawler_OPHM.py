from json import loads
from urllib3 import PoolManager


def conversor(valor):
    return float(valor[0:4].replace(",", '.'))


def request_temperature():
    with PoolManager() as pool:

        response = pool.request('GET', 'http://localhost:9000/data.json')
        data = loads(response.data.decode('utf-8'))

        tamanho = 0
        soma = 0

        for i in data['Children'][0]['Children'][1]['Children'][1]['Children']:

            print(f"{i['Text']}: Temperatura Atual >>> {conversor(i['Value'])} °C")
            soma += conversor(i['Value'])
            tamanho += 1

        return soma / tamanho
