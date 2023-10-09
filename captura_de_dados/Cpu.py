import psutil as ps
from acesso_banco.registro_dao import inserir_registro
import datetime as dt


class Cpu:

    def get_cpu_usage_percent(momento):
        cpu_percent = ps.cpu_percent()
        inserir_registro(4, 1, 2, cpu_percent, momento)

        return cpu_percent

    def get_cpu_frequency(momento):
        cpu_freq = (ps.cpu_freq().current * (10 ** -3))
        inserir_registro(4, 1, 4, cpu_freq, momento)

        return cpu_freq
    

    def get_cpu_status(momento):
        cpu_interrupcoes = ps.cpu_stats().interrupts
        print(cpu_interrupcoes)

