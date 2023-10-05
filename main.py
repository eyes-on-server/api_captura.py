from time import sleep as s
from captura_de_dados.Cpu import Cpu
from captura_de_dados.Memoria import Memoria
from captura_de_dados.Disco import Disco
from captura_de_dados.Rede import Rede

cpu = Cpu()
memoria = Memoria()
disco = Disco()
rede = Rede()


def start():

    while True:
        cpu.get_cpu_frequency()
        cpu.get_cpu_usage_percent()
        memoria.get_memory_usage_percent()
        disco.get_disk_usage_percent()
        rede.get_sent_bytes()
        rede.get_received_bytes()

        s(5)


start()
