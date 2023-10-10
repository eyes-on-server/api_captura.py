# EXECUTE ESSE ARQUIVO
from time import sleep as s
from captura_de_dados.Cpu import Cpu
from captura_de_dados.Memoria import Memoria
from captura_de_dados.Disco import Disco
from captura_de_dados.Rede import Rede
import datetime as dt

cpu = Cpu()
memoria = Memoria()
disco = Disco()
rede = Rede()


def start():

    while True:

        momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cpu.get_cpu_frequency(momento)
        cpu.get_cpu_usage_percent(momento)
        cpu.get_cpu_status()
        memoria.get_memory_usage_percent(momento)
        disco.get_disk_usage_percent(momento)
        rede.get_sent_bytes(momento)
        rede.get_received_bytes(momento)


        s(1)


start()
