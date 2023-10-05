import psutil
from acesso_banco.registro_dao import inserir_registro
import datetime as dt


class Memoria:
    def __init__(self):
        self.momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_memory_usage(self):
        self.momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        memory_usage = (psutil.virtual_memory().used * (10 ** -9))

        return memory_usage

    def get_memory_usage_percent(self):
        self.momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        memory_usage_percent = psutil.virtual_memory().percent
        inserir_registro(2, 2, 2, memory_usage_percent, self.momento)

        return memory_usage_percent
