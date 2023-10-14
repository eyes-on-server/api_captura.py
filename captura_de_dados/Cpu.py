import psutil as ps
from envio_mensagens.pipefy import enviar_mensagem
from dao.registro_dao import inserir_registro
from math import *


class Cpu:

    def get_cpu_usage_percent(self, momento):

        cpu_percent = ps.cpu_percent()
        cpu_percent_2 = round(cpu_percent + (cpu_percent * 0.05),1)
        cpu_percent_3 = round(cpu_percent / 2 - (cpu_percent * 0.1) - (cpu_percent_2 * 0.05),1)
        cpu_percent_4 = round(cpu_percent / 3 + (sqrt(cpu_percent_3) - sqrt(cpu_percent_2)) - (sin(cpu_percent)),1)
        cpu_percent_5 = round(cpu_percent - (cos(pow(cpu_percent_2, 2)) + cpu_percent_3 * 0.15) - (cpu_percent_4 * 0.10),1)
        cpu_percent_6 = round(cpu_percent + (cpu_percent_2 - cpu_percent_3 * 0.1) - sqrt(cpu_percent_5), 1)

        inserir_registro(1, 1, 2, cpu_percent, momento)
        inserir_registro(2, 1, 2, cpu_percent_2, momento)
        inserir_registro(3, 1, 2, cpu_percent_3, momento)
        inserir_registro(4, 1, 2, cpu_percent_4, momento)
        inserir_registro(5, 1, 2, cpu_percent_5, momento)
        inserir_registro(6, 1, 2, cpu_percent_6, momento)

        self.verificar_cpu(cpu_percent, momento, 1, 'F4-A2')
        self.verificar_cpu(cpu_percent, momento, 2, 'A3-B9')
        self.verificar_cpu(cpu_percent, momento, 3, 'E2-F0')
        self.verificar_cpu(cpu_percent, momento, 4, 'A5-B3')
        self.verificar_cpu(cpu_percent, momento, 5, 'C1-A1')
        self.verificar_cpu(cpu_percent, momento, 6, 'D4-D2')

        return cpu_percent

    def get_cpu_frequency(self, momento):

        cpu_freq = (ps.cpu_freq().current * (10 ** -3))
        cpu_freq_2 = cpu_freq * 2
        cpu_freq_3 = cpu_freq + (cpu_freq_2 * 0.15)
        cpu_freq_4 = cpu_freq - (sqrt(cpu_freq_3) * sin(cpu_freq_2))

        inserir_registro(1, 1, 4, cpu_freq, momento)
        inserir_registro(2, 1, 4, cpu_freq_2, momento)
        inserir_registro(3, 1, 4, cpu_freq_3, momento)
        inserir_registro(4, 1, 4, cpu_freq_4, momento)

        return cpu_freq

    def get_cpu_status(self):
        cpu_interrupcoes = ps.cpu_stats().interrupts
        print(cpu_interrupcoes)

    def verificar_cpu(self, cpu, momento, id_server, nome_servidor):

        tipo_alerta = ""

        if(cpu >= 95):
            tipo_alerta = "Emergência"
        elif(cpu >= 85):
            tipo_alerta = "Perigo"
        elif(cpu >= 75):
            tipo_alerta = "Prevenção"
        else:
            return

        titulo_alerta = f"Alerta: Cpu em Estado de {tipo_alerta}!"
        mensagem = (f"Detectamos que a CPU do servidor {nome_servidor} entrou no estado de {tipo_alerta}. "
                    f"Um chamado foi aberto na help desk de sua empresa para a solução rápida desse problema!")

        enviar_mensagem(titulo_alerta, mensagem, tipo_alerta, momento, id_server)
