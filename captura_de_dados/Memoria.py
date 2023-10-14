import psutil as ps
from envio_mensagens.pipefy import enviar_mensagem
from dao.registro_dao import inserir_registro
from math import *


class Memoria:

    def get_memory_usage(self, momento):

        memory_usage = (ps.virtual_memory().used * (10 ** -9))

        return memory_usage

    def get_memory_usage_percent(self, momento):

        memory_usage_percent = ps.virtual_memory().percent
        memory_usage_percent_2 = round(memory_usage_percent / 4, 1)
        memory_usage_percent_3 = round(memory_usage_percent_2 + (memory_usage_percent * 0.5), 1)
        memory_usage_percent_4 = round(
            (memory_usage_percent_3 / sqrt(memory_usage_percent_2)) + (memory_usage_percent * 0.05), 1)
        memory_usage_percent_5 = round(memory_usage_percent - (memory_usage_percent_4 * 0.15) - (
                    memory_usage_percent_2 + (memory_usage_percent_3 / 5)), 1)
        memory_usage_percent_6 = round(memory_usage_percent_5 + (memory_usage_percent - (0.5 * memory_usage_percent_3)),
                                       1)

        inserir_registro(1, 2, 2, memory_usage_percent, momento)
        inserir_registro(2, 2, 2, memory_usage_percent_2, momento)
        inserir_registro(3, 2, 2, memory_usage_percent_3, momento)
        inserir_registro(4, 2, 2, memory_usage_percent_4, momento)
        inserir_registro(5, 2, 2, memory_usage_percent_5, momento)
        inserir_registro(6, 2, 2, memory_usage_percent_6, momento)

        return memory_usage_percent

    def verificar_memoria(self, memoria, momento, id_server, nome_servidor):

        tipo_alerta = ""

        if (memoria >= 80):
            tipo_alerta = "Emergência"
        elif (memoria >= 75):
            tipo_alerta = "Perigo"
        elif (memoria >= 70):
            tipo_alerta = "Prevenção"
        else:
            return

        titulo_alerta = f"Alerta: Memória em Estado de {tipo_alerta}!"
        mensagem = (f"Detectamos que a Memória do servidor {nome_servidor} entrou no estado de {tipo_alerta}. "
                    f"Um chamado foi aberto na help desk de sua empresa para a solução rápida desse problema!")

        enviar_mensagem(titulo_alerta, mensagem, tipo_alerta, momento, id_server)