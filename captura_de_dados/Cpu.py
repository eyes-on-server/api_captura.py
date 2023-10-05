import psutil
from acesso_banco.registro_dao import inserir_registro
import datetime as dt


class Cpu:

    def __init__(self):
        self.momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_cpu_usage_percent(self):
        self.momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cpu_percent = psutil.cpu_percent()
        inserir_registro(2, 1, 2, cpu_percent, self.momento)

        return cpu_percent

    def get_cpu_frequency(self):
        self.momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cpu_freq = (psutil.cpu_freq().current * (10 ** -3))
        inserir_registro(2, 1, 4, cpu_freq, self.momento)

        return cpu_freq
