import psutil as ps
from interfaces import Executavel
from crawler.crawler_OPHM import request_temperature
import platform as plt


class CpuTemperatura(Executavel.Executavel):

    def executar(self):

        if plt.system() == 'Linux':
            cpu_temp = ps.sensors_temperatures()['coretemp'][0].current
        else:
            cpu_temp = request_temperature()

        return cpu_temp
