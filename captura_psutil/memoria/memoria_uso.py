import psutil as ps
from interfaces import Executavel


class MemoriaUso(Executavel.Executavel):

    def executar(self):
        memoria_uso = ps.virtual_memory().percent
        print(memoria_uso)
