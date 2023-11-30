from json import loads
from urllib3 import PoolManager


def conversor(valor):
    return float(valor[0:4].replace(",", '.'))


def request_temperature():

    tamanho = 0
    soma = 0

    with PoolManager() as pool:

        try:
            response = pool.request('GET', 'http://localhost:9000/data.json')
            data = loads(response.data.decode('utf-8'))

            for i in data['Children'][0]['Children'][1]['Children'][1]['Children']:

                print(f"{i['Text']}: Temperatura Atual >>> {conversor(i['Value'])} °C")
                soma += conversor(i['Value'])
                tamanho += 1
        except IndexError as erro:
            print('Erro! Não foi possível capturar a temperatura da sua máquina com o Open Hardware Monitor! ', erro)
        except Exception as erro:
            print('Não foi possível efetuar a conexão com o Open Hardware Monitor! ', erro)

        return soma / tamanho if tamanho > 0 else 0
