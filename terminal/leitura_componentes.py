from enumerators.componentes_monitorados import ComponentesMonitorados
from dao.servidor_dao import *
from dao.view_componente_servidor import *
from dao.login_dao import realizar_login
from terminal.novo_dispositivo import cadastrar_novo_servidor
from utils.informacoes_maquina import get_mac_address

mac_address = get_mac_address()


def autenticar_maquina():

    fk_empresa = login()

    if len(consultar_servidor(mac_address)) == 0:
        print("Servidor não encontrado, iniciando cadastro...\n")
        cadastrar_novo_servidor(fk_empresa, mac_address)

    print("\nIniciando leitura dos componentes!\n")

    return obter_executaveis()


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
