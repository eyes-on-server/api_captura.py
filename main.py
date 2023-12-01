# EXECUTE ESSE ARQUIVO

from terminal.leitura_componentes import *
from time import sleep
import datetime as dt
from captura_processos.processos import get_processos
from dao.registro_dao import *
from dao.servidor_dao import consultar_servidor
from dao.componente_medida_dao import coletar_metricas
import utils.funcoes_especiais_projeto as utils
from threading import Thread
from envio_mensagens.pipefy import enviar_mensagem


def iniciar_leitura():
    executaveis = lista_executaveis
    ticks = 0

    while True:

        momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for executavel in executaveis:
            id_componente_servidor = coletar_id_componente_servidor(mac_address, executavel.name)[0][0]
            valor = executavel.value["metodo"].executar()

            inserir_registro(id_componente_servidor, valor, momento)
            print(f'{executavel.value["nome"]}: {valor}')

            verificar_metricas(executavel, valor, momento)

        print('\n')

        ticks += 1

        if ticks == 3:
            executaveis = obter_executaveis()
            ticks = 0

        utils.verificar_downtime()
        utils.calcular_consumo_geral_servidor()

        sleep(10)


def ler_processos():
    while True:
        get_processos(consultar_servidor(mac_address)[0][0])
        sleep(10)


def verificar_metricas(executavel, valor, momento):
    metricas = coletar_metricas(executavel.name)[0]
    tipo_alerta = ""

    if metricas[0] is not None:
        if valor >= metricas[0]:
            tipo_alerta = "Emergência"
        elif valor >= metricas[1]:
            tipo_alerta = "Perigo"
        elif valor >= metricas[2]:
            tipo_alerta = "Prevenção"
        else:
            print("Componente não apresenta alerta!")

    if tipo_alerta != "":
        enviar_mensagem(tipo_alerta, momento, executavel, valor)


lista_executaveis = autenticar_maquina()

processo_leitura_registros = Thread(target=iniciar_leitura)
processo_leitura_processos = Thread(target=ler_processos)

processo_leitura_registros.start()
processo_leitura_processos.start()

print('Finalizando!')
