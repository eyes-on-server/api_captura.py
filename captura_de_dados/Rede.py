import psutil
from acesso_banco.registro_dao import inserir_registro


class Rede:
    def get_sent_bytes(momento):
        sent_bytes = psutil.net_io_counters().bytes_sent
        inserir_registro(4, 4, 6, sent_bytes, momento)

        return sent_bytes

    def get_received_bytes(momento):
        received_bytes = psutil.net_io_counters().bytes_recv
        inserir_registro(4, 4, 7, received_bytes, momento)

        return received_bytes
