import psutil
from acesso_banco.registro_dao import inserir_registro
import datetime as dt
import platform as plt
from math import *

caminho = ''

if plt.system() == 'Linux':
    caminho = '/'
elif plt.system() == 'Windows':
    caminho = 'C:\\'


class Disco:
    def __init__(self):
        self.caminho = caminho

    def get_disk_usage(self):

        disk_usage = (psutil.disk_usage(self.caminho).used * (10 ** -9))

        return disk_usage

    def get_disk_usage_percent(self, momento):

        disk_usage_percent = psutil.disk_usage(caminho).percent
        disk_usage_percent_2 = round(disk_usage_percent / 2, 1)
        disk_usage_percent_3 = round(disk_usage_percent + (disk_usage_percent_2 * 0.05) + (sqrt(disk_usage_percent)), 1)
        disk_usage_percent_4 = round(0.7 * disk_usage_percent, 1)
        disk_usage_percent_5 = round(disk_usage_percent - disk_usage_percent_4, 1)
        disk_usage_percent_6 = round(
            disk_usage_percent - (sqrt(disk_usage_percent_5) + 3) - (0.15 * disk_usage_percent_3), 1)

        inserir_registro(1, 3, 2, disk_usage_percent, momento)
        inserir_registro(2, 3, 2, disk_usage_percent_2, momento)
        inserir_registro(3, 3, 2, disk_usage_percent_3, momento)
        inserir_registro(4, 3, 2, disk_usage_percent_4, momento)
        inserir_registro(5, 3, 2, disk_usage_percent_5, momento)
        inserir_registro(6, 3, 2, disk_usage_percent_6, momento)

        return disk_usage_percent
    