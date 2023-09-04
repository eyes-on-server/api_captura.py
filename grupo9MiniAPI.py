import psutil
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mysql.connector
import platform

# Criando a tela para plotagem do gráfico
# Onde: canvas -> é a tela para plotagem
#       [n1, n2, n3, n...] -> qtd de subplotagens da tela
#       plt.subplots(n1, n2) -> n1 = nº de subplotagens desejadas; n2 = nº de dimensões
canvas, [axCPU, axRAM, axDisco] = plt.subplots(3, 1)

canvas.subplots_adjust(hspace=1) # Espaçamento entre os gráficos

eixo_x_CPU = []
eixo_y_CPU = []

eixo_x_RAM = []
eixo_y_RAM = []

eixo_x_Disco = []
eixo_y_Disco = []


user = input("Digite o nome de usuário do Banco de dados: ")
senha = input("Digite a senha do Banco de Dados: ")

mydb = mysql.connector.connect(
    host="localhost",
    user=user,
    password=senha
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS `registro`;")
mycursor.execute("USE registro;")

mycursor.execute(
    """
        CREATE TABLE IF NOT EXISTS `CPU` (
        idCPU INT PRIMARY KEY AUTO_INCREMENT,
        valor INT,
        horario TIME
        ); 
    """
)

mycursor.execute(
    """
        CREATE TABLE IF NOT EXISTS `RAM` (
            idRAM INT PRIMARY KEY AUTO_INCREMENT,
            valor INT,
            horario TIME
        );
        """
)

mycursor.execute(
    """
        CREATE TABLE IF NOT EXISTS `disco` (
        idDisco INT PRIMARY KEY AUTO_INCREMENT,
        valor INT,
        horario TIME
        );
    """
)


def insert_CPU():
    # Capturar a % de uso da CPU
    cpuPercent = psutil.cpu_percent()
    horarioAtual = dt.datetime.now().strftime('%H:%M:%S')

    comando = f"INSERT INTO `CPU` VALUES (null, {cpuPercent}, '{horarioAtual}');"
    mycursor.execute(comando)
    mydb.commit()


def insert_RAM():
    memoryUsage =  psutil.virtual_memory()
    horarioAtual = dt.datetime.now().strftime('%H:%M:%S')

    comando = f"INSERT INTO `RAM` VALUES (null, {memoryUsage.percent}, '{horarioAtual}');"
    mycursor.execute(comando)
    mydb.commit()


def insert_disco():
    if platform.system() == "Linux":
        caminho = '/'
    else:
        caminho = 'C:\\'
    diskUsage = psutil.disk_usage(caminho)
    horarioAtual = dt.datetime.now().strftime('%H:%M:%S')
    
    comando = f"INSERT INTO `disco` VALUES (null, {diskUsage.percent}, '{horarioAtual}');"
    mycursor.execute(comando)
    mydb.commit()


def plotar_grafico(i,insert_function, eixo_x, eixo_y,  subplot, select, dispositivo):
    print(select)
    #Fazer o insert
    insert_function()

    # Adicionando o horário e a % de uso da CPU para os eixos x, y
    mycursor.execute(select)

    myresult = mycursor.fetchall()
    
    # Limitando a quantidade de dados a serem exibidos
    if len(eixo_x) < 10:
        eixo_y.append(myresult[-1][1])
        eixo_x.append(str(myresult[-1][2]))
    else:
        del eixo_x[0]
        eixo_y.append(myresult[-1][1])
        del eixo_y[0]
        eixo_x.append(str(myresult[-1][2]))
    
    # Plotagem do gráfico
    subplot.clear()
    subplot.plot(eixo_x, eixo_y)

    # Título e legendas
    subplot.set_title(f'Uso da {dispositivo}')
    subplot.set_ylabel(f'{dispositivo} (%)')


# Chamada recursiva da função com (lugar onde irá ser plotado, eixos, intervalo)
grafico_CPU = animation.FuncAnimation(canvas, plotar_grafico, fargs=(insert_CPU,eixo_x_CPU, eixo_y_CPU, axCPU, "SELECT * FROM CPU", "CPU"), interval=1000)
grafico_RAM = animation.FuncAnimation(canvas, plotar_grafico, fargs=(insert_RAM,eixo_x_RAM, eixo_y_RAM, axRAM, "SELECT * FROM RAM", "RAM"), interval=1000)
grafico_disco = animation.FuncAnimation(canvas, plotar_grafico, fargs=(insert_disco,eixo_x_Disco, eixo_y_Disco, axDisco, "SELECT * FROM disco", "Disco"), interval=1000)
plt.show()
