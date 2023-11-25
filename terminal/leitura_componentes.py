from enumerators.componentes_monitorados import ComponentesMonitorados
from dao.servidor_dao import *
from dao.view_componente_servidor import *
from dao.login_dao import realizar_login
from dao.registro_dao import inserir_registro
from terminal.novo_dispositivo import cadastrar_novo_servidor

from time import sleep
import psutil as ps
import datetime as dt

mac_address = ps.net_if_addrs()['Ethernet'][0].address


def run():

    fk_empresa = login()

    if len(consultar_servidor(mac_address)) == 0:
        print("Servidor não encontrado, iniciando cadastro...\n")
        cadastrar_novo_servidor(fk_empresa, mac_address)

    print("\nIniciando leitura dos componentes!\n")

    iniciar_leitura(obter_executaveis())


def login():
    while True:
        print("Login no Sistema")

        login = str(input("Login: "))
        senha = str(input("Senha: "))

        resultados_obtidos = realizar_login(login, senha)

        if len(resultados_obtidos) == 0:
            print("\nAcesso negado\n")
        else:
            print("\nAcesso permitido\n")
            return resultados_obtidos[0][0]


def obter_executaveis():

    lista_componentes_monitorados = []
    lista_componente_servidor = consultar_componente_servidor(mac_address)
    lista_executaveis = []

    for componente in ComponentesMonitorados:
        lista_componentes_monitorados.append(componente)

    for componente_monitorado in lista_componentes_monitorados:
        for componente_servidor in lista_componente_servidor:
            if componente_monitorado.name == componente_servidor[5]:
                lista_executaveis.append(componente_monitorado)
                break

    return lista_executaveis


def iniciar_leitura(lista_executaveis):

    executaveis = lista_executaveis
    ticks = 0

    while True:

        momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for executavel in executaveis:
            id_componente_servidor = coletar_id_componente_servidor(mac_address, executavel.name)[0][0]
            valor = executavel.value["metodo"].executar()

            inserir_registro(id_componente_servidor, valor, momento)

        ticks += 1

        if ticks == 3:
            executaveis = obter_executaveis()
            ticks = 0

        sleep(10)
