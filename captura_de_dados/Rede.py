import psutil
from acesso_banco.registro_dao import inserir_registro
import datetime as dt


class Rede:
    def __init__(self):
        self.momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_sent_bytes(self):
        self.momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        sent_bytes = psutil.net_io_counters().bytes_sent
        inserir_registro(2, 4, 6, sent_bytes, self.momento)

        return sent_bytes

    def get_received_bytes(self):
        self.momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        received_bytes = psutil.net_io_counters().bytes_recv
        inserir_registro(2, 4, 7, received_bytes, self.momento)

        return received_bytes
