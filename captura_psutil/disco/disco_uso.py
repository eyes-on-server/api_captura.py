import psutil as ps
from interfaces import Executavel


class DiscoUso(Executavel.Executavel):

    def executar(self):
        particoes = ps.disk_partitions()
        total = 0

        for particao in particoes:
            total += ps.disk_usage(particao.device).percent

        uso_disco = total / len(particoes)

        return uso_disco
