# EXECUTE ESSE ARQUIVO
# from time import sleep as s
# from captura_processos.Processos import Processos
# import datetime as dt
#
# processos = Processos()
#
#
# def start():
#
#     while True:
#
#         momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#
#         processos.get_processos()
#
#         s(5)


# start()

from enumerators.componentes_monitorados import ComponentesMonitorados
from dao.servidor_dao import *
from dao.login_dao import realizar_login
import psutil as ps
import os

fk_empresa = 0
mac_addres = ps.net_if_addrs()['Ethernet'][0].address
ipv6 = ps.net_if_addrs()['Ethernet'][2].address
sistema_operacional = os.name

while True:
    print("Login no Sistema")

    login = str(input("Login: "))
    senha = str(input("Senha: "))

    resultados_obtidos = realizar_login(login, senha)

    if len(resultados_obtidos) == 0:
        print("Acesso negado")
        print('\n')

    else:
        print("Acesso permitido")
        print('\n')

        fk_empresa = resultados_obtidos[0][0]
        break

if len(consultar_servidor(mac_addres)) == 0:
    nome_servidor = str(input("Nome Servidor: "))
    local_servidor = str(input("Local do Servidor: "))
    descricao_servidor = str(input("Descrição do Servidor: "))

    cadastrar_servidor(
        fk_empresa,
        nome_servidor,
        local_servidor,
        ipv6,
        mac_addres,
        sistema_operacional,
        descricao_servidor
    )

lista_componentes_monitorados = []

for componente in ComponentesMonitorados:
    lista_componentes_monitorados.append(componente.name)

print("\nSelecione os componentes que gostaria de monitorar:")

while True:

    print(lista_componentes_monitorados)
    
    if len(lista_componentes_monitorados) == 0:
        break

    i = 0
    for i in range(len(lista_componentes_monitorados)):
        print(f'{i+1} - {lista_componentes_monitorados[i]}')

    print(f'{i+2} - Finalizar')

    opcao = int(input("Sua opção: "))

    if opcao == i+2:
        break

    lista_componentes_monitorados.pop(opcao)



