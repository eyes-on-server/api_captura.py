import psutil
import datetime as dt
import platform
from time import sleep as s
from acesso_banco.registro_dao import inserir_registro

# import slack
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation


# Criando a tela para plotagem do gráfico
# Onde: canvas -> é a tela para plotagem
#       [n1, n2, n3, n...] -> qtd de subplotagens da tela
#       plt.subplots(n1, n2) -> n1 = nº de subplotagens desejadas; n2 = nº de dimensões
# canvas, [cpu, ram, disco] = plt.subplots(3, 1)

# canvas.subplots_adjust(hspace=1) # Espaçamento entre os gráficos

# eixo_x_cpu = []
# eixo_y_cpu = []
#
# eixo_x_ram = []
# eixo_y_ram = []
#
# eixo_x_disco = []
# eixo_y_disco = []


def get_cpu():
    cpu_freq = psutil.cpu_freq().current * 10**-3
    cpu_percent = psutil.cpu_percent()
    momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    inserir_registro(6,1, 2, cpu_percent, momento)
    inserir_registro(6,1, 4, cpu_freq, momento)

    # alert = f"""
    # ATENÇÃO!
    # Sua CPU entrou em estado de alerta.
    # Porcentagem atual: {str(cpu_percent)}
    # """

    # desc = f"""
    # Cpu está em um nível muito elevado de frequência.
    # Frequência bruta: {str(round(cpu_freq,2))}
    # Frequência em porcentagem: {str(cpu_percent)}
    # """

    # sum = "Sua CPU entrou em estado de alerta."

    # if cpu_percent > 50 and cpu_percent < 70:
    #     slack.slack_alerta(alert)
    # else:
    #     slack.slack_alerta(alert)
    #     chamado_jira.chamado(sum, desc)


def get_ram():
    memory_usage = psutil.virtual_memory().used * 10**-9
    memory_usage_percent = psutil.virtual_memory().percent
    momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    inserir_registro(6,2, 2, memory_usage_percent, momento)

    # alert = f"""
    # ATENÇÃO!
    # Sua RAM entrou em estado de alerta.
    # Porcentagem atual: {str(memory_usage_percent)}"
    # """

    # desc = f"""
    # Foi monitorado que a ram está ficando sem espaço.
    # Ram consumida: {str(round(memory_usage,2))}
    # Ram em porcentagem: {str(memory_usage_percent)}
    # """

    # sum = "Sua RAM entrou em estado de alerta."

    # if memory_usage_percent > 50 and memory_usage_percent < 70:
    #     slack.slack_alerta(alert)
    # else:
    #     slack.slack_alerta(alert)
    #     chamado_jira.chamado(sum, desc)


def get_disco():

    caminho = ''

    if platform.system() == "Linux":
        caminho = '/'
    elif platform.system() == "Windows":
        caminho = 'C:\\'

    disk_usage = psutil.disk_usage(caminho).used * 10**-9
    disk_usage_percent = psutil.disk_usage(caminho).percent
    momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    inserir_registro(6,3,2,disk_usage_percent, momento)

    # alert = f"""
    # ATENÇÃO!
    # Seu disco entrou em estado de alerta.
    # Porcentagem atual: {str(disk_usage_percent)}
    # """

    # desc = f"""
    # Foi identificado que seu disco está com pouco espaço.
    # Espaço de disco consumido: {str(round(disk_usage,2))}
    # Disco em porcentagem: {str(disk_usage_percent)}
    # """

    # sum = "Seu disco entrou em estado de alerta."

    # if disk_usage_percent > 60 and disk_usage_percent < 80:
    #     slack.slack_alerta(alert)
    # else:
    #     slack.slack_alerta(alert)
    #     chamado_jira.chamado(sum, desc)


def start():
    while True:
        get_cpu()
        get_ram()
        get_disco()

        s(5)

# def plotar_grafico(i,insert_function, eixo_x, eixo_y,  subplot, select, dispositivo):
#     print(1)
#     print(select)
#     print(2)

#     Fazer o insert
#     insert_function()

#     # Adicionando o horário e a % de uso da cpu para os eixos x, y
#     executar(select)

#     result = executar.fetchall()

#     Limitando a quantidade de dados a serem exibidos
#     if len(eixo_x) < 10:
#         eixo_y.append(result[-1][1])
#         eixo_x.append(str(result[-1][2]))
#     else:
#         del eixo_x[0]
#         eixo_y.append(result[-1][1])
#         del eixo_y[0]
#         eixo_x.append(str(result[-1][2]))

#     Plotagem do gráfico
#     subplot.clear()
#     subplot.plot(eixo_x, eixo_y)

#     Título e legendas
#     subplot.set_title(f'Uso da {dispositivo}')
#     subplot.set_ylabel(f'{dispositivo} (%)')

# Chamada recursiva da função com (lugar onde irá ser plotado, eixos, intervalo)

# grafico_cpu = animation.FuncAnimation(canvas, plotar_grafico, fargs=(insert_cpu,eixo_x_cpu, eixo_y_cpu, cpu,
# "select valor_registro from Eyes_On_Server.Registro Where fk_componente = 1;", "cpu"), interval=1000)

# grafico_ram = animation.FuncAnimation(canvas, plotar_grafico, fargs=(insert_ram,eixo_x_ram, eixo_y_ram, ram,
# "select valor_registro from Eyes_On_Server.Registro Where fk_componente = 2;", "ram"), interval=1000)

# grafico_disco = animation.FuncAnimation(canvas, plotar_grafico, fargs=(insert_disco,eixo_x_disco, eixo_y_disco, disco,
# "select valor_registro from Eyes_On_Server.Registro Where fk_componente = 3;", "disco"), interval=1000)

# plt.show()
