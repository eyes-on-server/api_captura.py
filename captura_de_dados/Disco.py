import psutil
from acesso_banco.registro_dao import inserir_registro
import datetime as dt
import platform as plt


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
        self.momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        disk_usage_percent = psutil.disk_usage(caminho).percent
        inserir_registro(4, 3, 2, disk_usage_percent, momento)

        return disk_usage_percent
    