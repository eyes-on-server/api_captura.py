import psutil
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import platform
# import mysql.connector as sql
# import mysql.connector.errorcode
# import chamado_jira
# import slack
from connection import executar


# Criando a tela para plotagem do gráfico
# Onde: canvas -> é a tela para plotagem
#       [n1, n2, n3, n...] -> qtd de subplotagens da tela
#       plt.subplots(n1, n2) -> n1 = nº de subplotagens desejadas; n2 = nº de dimensões
canvas, [cpu, ram, disco] = plt.subplots(3, 1)

canvas.subplots_adjust(hspace=1) # Espaçamento entre os gráficos

eixo_x_cpu = []
eixo_y_cpu = []

eixo_x_ram = []
eixo_y_ram = []

eixo_x_disco = []
eixo_y_disco = []



def insert_cpu():
    print("Lendo cpu")
    # Capturar a % de uso da cpu
    cpu_freq = psutil.cpu_freq().current * 10**-3
    cpu_percent = psutil.cpu_percent()
    horario_atual =dt.datetime.now().strftime('%y/%m/%d %H:%M:%S')

    alert = "ATENÇÃO! \nSua cpu entrou em estado de alerta. \nPorcentagem atual: " + str(cpu_percent)
    desc = "cpu está em um nível muito elevado de frequência. \nFrequência bruta: " + str(round(cpu_freq,2)) + "\nFrequência em porcentagem: " + str(cpu_percent)
    sum = "Sua cpu entrou em estado de alerta."

    # if cpu_percent > 50 and cpu_percent < 70:
        # slack.slack_alerta(alert)
    # else:
        # slack.slack_alerta(alert)
        # chamado_jira.chamado(sum, desc)
  

    
    query = "INSERT INTO Eyes_On_Server.Registro(id_registro, fk_componente, fk_medida, valor_registro, momento_registro) VALUES (null, 1, 2, %s, %s);"
    values = [cpu_percent, horario_atual]
    executar(query, values)
    print("inserindo no banco")


def insert_ram():
    print("Lendo ram")

    memory_usage = psutil.virtual_memory().used * 10**-9
    memory_usage_percent = psutil.virtual_memory().percent
    horario_atual =dt.datetime.now().strftime('%y/%m/%d %H:%M:%S')

    alert = "ATENÇÃO! \nSua ram entrou em estado de alerta. \nPorcentagem atual: " + str(memory_usage_percent)
    desc = "Foi monitorado que a ram está ficando sem espaço. \nram consumida: " + str(round(memory_usage,2)) + "\nram em porcentagem: " + str(memory_usage_percent)
    sum = "Sua ram entrou em estado de alerta."


    # if memory_usage_percent > 50 and memory_usage_percent < 70:
    #     slack.slack_alerta(alert)
    # else:
    #     slack.slack_alerta(alert)
    #     chamado_jira.chamado(sum, desc)

    
    query = "INSERT INTO Eyes_On_Server.Registro(id_registro, fk_componente, fk_medida, valor_registro, momento_registro) VALUES (null, 2, 2, %s, %s);"
    values = [memory_usage_percent, horario_atual]
    executar(query, values)
    print("inserindo ram no banco")



def insert_disco():
    print("Lendo disco")

    if platform.system() == "Linux":
        caminho = '/'
    else:
        caminho = 'C:\\'
    disk_usage = psutil.disk_usage(caminho).used * 10**-9
    disk_usage_percent = psutil.disk_usage(caminho).percent
    horario_atual =dt.datetime.now().strftime('%y/%m/%d %H:%M:%S')

    alert = "ATENÇÃO! \nSeu disco entrou em estado de alerta. \nPorcentagem atual: " + str(disk_usage_percent)
    desc = "Foi identificado que seu disco está com pouco espaço. \nEspaço de disco consumido: " + str(round(disk_usage,2)) + "\ndisco em porcentagem: " + str(disk_usage_percent)
    sum = "Seu disco entrou em estado de alerta."

    # if disk_usage_percent > 60 and disk_usage_percent < 80:
    #     slack.slack_alerta(alert)
    # else:
    #     slack.slack_alerta(alert)
    #     chamado_jira.chamado(sum, desc)
    

    query = "INSERT INTO Eyes_On_Server.Registro(id_registro, fk_componente, fk_medida, valor_registro, momento_registro) VALUES (null, 3, 2, %s, %s);"
    values = [disk_usage_percent, horario_atual]
    executar(query, values)
    print("inserindo ram no disco")



def plotar_grafico(i,insert_function, eixo_x, eixo_y,  subplot, select, dispositivo):
    print(1)
    print(select)
    print(2)

    #Fazer o insert
    insert_function()

    # Adicionando o horário e a % de uso da cpu para os eixos x, y
    executar(select)

    result = executar.fetchall()
    
    # Limitando a quantidade de dados a serem exibidos
    if len(eixo_x) < 10:
        eixo_y.append(result[-1][1])
        eixo_x.append(str(result[-1][2]))
    else:
        del eixo_x[0]
        eixo_y.append(result[-1][1])
        del eixo_y[0]
        eixo_x.append(str(result[-1][2]))
    
    # Plotagem do gráfico
    subplot.clear()
    subplot.plot(eixo_x, eixo_y)

    # Título e legendas
    subplot.set_title(f'Uso da {dispositivo}')
    subplot.set_ylabel(f'{dispositivo} (%)')


# Chamada recursiva da função com (lugar onde irá ser plotado, eixos, intervalo)
grafico_cpu = animation.FuncAnimation(canvas, plotar_grafico, fargs=(insert_cpu,eixo_x_cpu, eixo_y_cpu, cpu, "select valor_registro from Eyes_On_Server.Registro Where fk_componente = 1;", "cpu"), interval=1000)
grafico_ram = animation.FuncAnimation(canvas, plotar_grafico, fargs=(insert_ram,eixo_x_ram, eixo_y_ram, ram, "select valor_registro from Eyes_On_Server.Registro Where fk_componente = 2;", "ram"), interval=1000)
grafico_disco = animation.FuncAnimation(canvas, plotar_grafico, fargs=(insert_disco,eixo_x_disco, eixo_y_disco, disco, "select valor_registro from Eyes_On_Server.Registro Where fk_componente = 3;", "disco"), interval=1000)
plt.show()
