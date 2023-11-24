import psutil as ps
from interfaces import Executavel


class RedeBytesRecebidos(Executavel.Executavel):

    def executar(self):
        rede_bytes_recebidos = ps.net_io_counters().bytes_recv
        print(rede_bytes_recebidos)
