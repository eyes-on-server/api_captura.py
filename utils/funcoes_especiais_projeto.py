from dao.downtime_dao import inserir_downtime
import psutil as ps
from dao.servidor_dao import consultar_servidor
from dao.registro_dao import *
from captura_psutil.cpu.cpu_uso import *
from captura_psutil.memoria.memoria_uso import *
from captura_psutil.disco.disco_uso import *


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


def calcular_consumo_geral_servidor(memoria_uso, cpu_percent, uso_disco):
     while True:

        limite_cpu = 0.7  
        limite_memo = 0.7  
        limite_disco = 0.7  

        consumo_geral = (cpu_percent * limite_cpu) - (memoria_uso * limite_memo) - (uso_disco * limite_disco)
        consumo_geral = consumo_geral *(-1)

        print("Consumo total da máquina: {:.2f}%".format(consumo_geral))
 