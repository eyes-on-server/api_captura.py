import psutil as ps
from interfaces import Executavel


class DiscoUso(Executavel.Executavel):

    def executar(self):
        particoes = ps.disk_partitions()
        print(particoes)
