import psutil as ps
from interfaces import Executavel


class RedeBytesEnviados(Executavel.Executavel):

    def executar(self):
        rede_bytes_enviados = ps.net_io_counters().bytes_sent
        return rede_bytes_enviados
