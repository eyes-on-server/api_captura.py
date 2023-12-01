import psutil as ps
from interfaces import Executavel
from crawler.crawler_OPHM import request_temperature
import platform as plt


class CpuTemperatura(Executavel.Executavel):

    def executar(self):

        if plt.system() == 'Linux':
            try:
                soma = 0
                for key in ps.sensors_temperatures().keys():
                    soma += ps.sensors_temperatures()[key][0].current
                cpu_temp = soma / len(ps.sensors_temperatures().keys())
            except Exception as erro:
                print('Não foi possível ler a temperatura: ', erro)
                cpu_temp = 0
        else:
            cpu_temp = request_temperature()

        return cpu_temp
