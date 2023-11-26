# EXECUTE ESSE ARQUIVO

from terminal.leitura_componentes import *
from time import sleep
import datetime as dt
from captura_processos.processos import get_processos
from dao.registro_dao import *
from dao.servidor_dao import consultar_servidor
from dao.downtime_dao import inserir_downtime
import psutil as ps


def verificar_downtime():

    fk_servidor = consultar_servidor(ps.net_if_addrs()['Ethernet'][0].address)[0][0]
    ultimo_momento_registro = ultimo_registro(fk_servidor)[0][0]
    penultimo_momento_registro = penultimo_registro(fk_servidor, ultimo_momento_registro)[0][0]

    margem = 25
    prejuizo_por_segundo = 1111111.1

    if penultimo_momento_registro is not None and ultimo_momento_registro is not None:
        diferenca = (ultimo_momento_registro - penultimo_momento_registro).total_seconds()

        if diferenca > margem:
            inserir_downtime(fk_servidor, diferenca - 20, (diferenca - 20) * prejuizo_por_segundo)


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

        verificar_downtime()
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
