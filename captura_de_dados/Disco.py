import psutil
from envio_mensagens.pipefy import enviar_mensagem
from dao.registro_dao import inserir_registro
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

    def verificar_disco(self, disco, momento, id_server, nome_servidor):

        tipo_alerta = ""

        if(disco >= 95):
            tipo_alerta = "Emergência"
        elif(disco >= 90):
            tipo_alerta = "Perigo"
        elif(disco >= 85):
            tipo_alerta = "Prevenção"
        else:
            return

        titulo_alerta = f"Alerta: Disco em Estado de {tipo_alerta}!"
        mensagem = (f"Detectamos que o Disco do servidor {nome_servidor} entrou no estado de {tipo_alerta}. "
                    f"Um chamado foi aberto na help desk de sua empresa para a solução rápida desse problema!")

        enviar_mensagem(titulo_alerta, mensagem, tipo_alerta, momento, id_server)