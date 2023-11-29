import math

from dao.componente_medida_dao import consultar_componente_medida
from dao.componente_servidor_dao import inserir_componente_servidor
from dao.servidor_dao import *
from enumerators.componentes_monitorados import ComponentesMonitorados
from utils.informacoes_maquina import get_ipv6
import os


def cadastrar_novo_servidor(fk_empresa, mac_address):

    cadastrar(fk_empresa, mac_address)

    fk_servidor = consultar_servidor(mac_address)[0][0]

    lista_componentes_monitorados = []

    for componente in ComponentesMonitorados:
        lista_componentes_monitorados.append(componente)

    componentes_selecionados = selecionar_componentes(lista_componentes_monitorados)

    for componentes_selecionado in componentes_selecionados:
        inserir_componente_servidor(fk_servidor, consultar_componente_medida(componentes_selecionado.name)[0][0])

    print("\nServidor cadastrado com sucesso!")


def cadastrar(fk_empresa, mac_address):

    ipv6 = get_ipv6()
    sistema_operacional = os.name

    nome_servidor = str(input("Nome Servidor: "))
    local_servidor = str(input("Local do Servidor: "))
    descricao_servidor = str(input("Descrição do Servidor: "))

    cadastrar_servidor(
        fk_empresa,
        nome_servidor,
        local_servidor,
        ipv6,
        mac_address,
        sistema_operacional,
        descricao_servidor
    )


def selecionar_componentes(lista_componentes_monitorados):

    componentes_selecionados = []

    while True:

        print("\nSelecione os componentes que gostaria de monitorar:")

        if len(lista_componentes_monitorados) == 0:
            break

        i = 0
        for i in range(len(lista_componentes_monitorados)):
            print(f'{i + 1} - {lista_componentes_monitorados[i].value["nome"]}')

        print(f'{i + 2} - Finalizar')

        try:
            opcao = int(input("Sua opção: "))
        except ValueError:
            opcao = 0

        if opcao == i + 2:
            break
        elif opcao <= 0 or opcao > len(lista_componentes_monitorados) or math.isnan(opcao):
            print("Digite um número dentro do intervalo informado!")
        else:
            componentes_selecionados.append(lista_componentes_monitorados[opcao - 1])
            lista_componentes_monitorados.pop(opcao - 1)

    return componentes_selecionados
