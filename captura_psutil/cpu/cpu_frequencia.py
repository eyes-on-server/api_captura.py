import psutil as ps
from interfaces import Executavel


class CpuFrequencia(Executavel.Executavel):

    def executar(self):
        cpu_freq = ps.cpu_freq().current
        return cpu_freq
