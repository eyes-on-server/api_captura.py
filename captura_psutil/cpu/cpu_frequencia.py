import psutil as ps
from interfaces import Executavel


class CpuFrequencia(Executavel.Executavel):

    def executar(self):
        cpu_freq = ps.cpu_freq().current
        print(cpu_freq)

        return cpu_freq
