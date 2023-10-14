import psutil
from dao.registro_dao import inserir_registro
from math import *


class Rede:
    def get_sent_bytes(self, momento):

        sent_bytes = psutil.net_io_counters().bytes_sent
        sent_bytes_2 = round((sent_bytes / 3), 0)
        sent_bytes_3 = round((sent_bytes + sent_bytes_2), 0)

        inserir_registro(1, 4, 6, sent_bytes, momento)
        inserir_registro(2, 4, 6, sent_bytes_2, momento)
        inserir_registro(3, 4, 6, sent_bytes_3, momento)

        return sent_bytes

    def get_received_bytes(self, momento):

        received_bytes = psutil.net_io_counters().bytes_recv
        received_bytes_2 = round((received_bytes + (received_bytes * 0.05)),0)
        received_bytes_3 = round((received_bytes - (sqrt(received_bytes_2) + received_bytes * 0.25)), 0)

        inserir_registro(1, 4, 7, received_bytes, momento)
        inserir_registro(2, 4, 7, received_bytes_2, momento)
        inserir_registro(3, 4, 7, received_bytes_3, momento)

        return received_bytes
