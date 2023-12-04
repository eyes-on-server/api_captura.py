import psutil as ps
from interfaces import Executavel


class DiscoUso(Executavel.Executavel):

    def executar(self):
        particoes = ps.disk_partitions()
        total = 0

        for particao in particoes:
            try:
                total += ps.disk_usage(particao.device).percent
            except Exception as e:
                print("Erro ao ler disco: ", e)

        uso_disco = total / len(particoes)

        return uso_disco
