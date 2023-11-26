# EXECUTE ESSE ARQUIVO

from terminal.leitura_componentes import *
from multiprocessing import Process
from time import sleep
import datetime as dt
from captura_processos.processos import get_processos
from dao.registro_dao import inserir_registro


def iniciar_leitura():

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


def ler_processos(fk_servidor):
    print('Lendo processos:')

    while True:
        get_processos(fk_servidor)
        sleep(10)


lista_executaveis = autenticar_maquina()

iniciar_leitura()
ler_processos(consultar_servidor(mac_address)[0][0])

print('Finalizando!')
