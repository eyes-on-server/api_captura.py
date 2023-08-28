import psutil
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mysql.connector

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

mycursor.execute("""CREATE TABLE IF NOT EXISTS `CPU` (
	idCPU INT PRIMARY KEY AUTO_INCREMENT,
    valor INT,
    horario TIME
    );"""
)

mycursor.execute("""CREATE TABLE IF NOT EXISTS `RAM` (
	idRAM INT PRIMARY KEY AUTO_INCREMENT,
    valor INT,
    horario TIME
    );"""
)

mycursor.execute("""CREATE TABLE IF NOT EXISTS `disco` (
	idDisco INT PRIMARY KEY AUTO_INCREMENT,
    valor INT,
    horario TIME
    );"""
)

def plotarGraficoCPU(i, eixo_x_CPU, eixo_y_CPU):

    # Capturar a % de uso da CPU
    cpuPercent = psutil.cpu_percent()
    horarioAtual = dt.datetime.now().strftime('%H:%M:%S')

    # Adicionando o horário e a % de uso da CPU para os eixos x, y
    eixo_x_CPU.append(horarioAtual)
    eixo_y_CPU.append(cpuPercent)
    
    # Limitando a quantidade de dados a serem exibidos
    eixo_x_CPU = eixo_x_CPU[-10:]
    eixo_y_CPU = eixo_y_CPU[-10:]

    # Plotagem do gráfico
    axCPU.clear()
    axCPU.plot(eixo_x_CPU, eixo_y_CPU)

    # Título e legendas
    axCPU.set_title('Uso da CPU')
    axCPU.set_ylabel('CPU (%)')

    print(f"CPU: ", cpuPercent, "%")
    comando = f"INSERT INTO `CPU` VALUES (null, {cpuPercent}, '{horarioAtual}');"
    mycursor.execute(comando)
    mydb.commit()



def plotarGraficoRAM(i, eixo_x_RAM, eixo_y_RAM):

    # Capturar a % de uso da RAM
    memoryUsage =  psutil.virtual_memory()
    horarioAtual = dt.datetime.now().strftime('%H:%M:%S')

    # Adicionando o horário e a % de uso da RAM para os eixos x, y
    eixo_x_RAM.append(horarioAtual)
    eixo_y_RAM.append(memoryUsage.percent)

    # Limitando a quantidade de dados a serem exibidos
    eixo_x_RAM = eixo_x_RAM[-10:]
    eixo_y_RAM = eixo_y_RAM[-10:]

    # Plotagem do gráfico
    axRAM.clear()
    axRAM.plot(eixo_x_RAM, eixo_y_RAM)

    # Título e legendas
    axRAM.set_title('Uso da RAM')
    axRAM.set_ylabel('RAM (%)')

    print(f"Memória: ", memoryUsage.percent, "%")
    comando = f"INSERT INTO `RAM` VALUES (null, {memoryUsage.percent}, '{horarioAtual}');"
    mycursor.execute(comando)
    mydb.commit()



def plotarGraficoDisco(i, eixo_x_Disco, eixo_y_Disco):

    # Capturar a % de uso do Disco
    diskUsage = psutil.disk_usage('C:\\')
    horarioAtual = dt.datetime.now().strftime('%H:%M:%S')

    # Adicionando o horário e a % de uso do Disco para os eixos x, y
    eixo_x_Disco.append(horarioAtual)
    eixo_y_Disco.append(diskUsage.percent)

    # Limitando a quantidade de dados a serem exibidos
    eixo_x_Disco = eixo_x_Disco[-10:]
    eixo_y_Disco = eixo_y_Disco[-10:]

    # Plotagem do gráfico
    axDisco.clear()
    axDisco.plot(eixo_x_Disco, eixo_y_Disco)

    # Título e legendas
    axDisco.set_title('Uso do Disco')
    axDisco.set_ylabel('Disco (%)')

    print(f"Disco: ", diskUsage.percent, "%")
    comando = f"INSERT INTO `disco` VALUES (null, {diskUsage.percent}, '{horarioAtual}');"
    mycursor.execute(comando)
    mydb.commit()


# Chamada recursiva da função com (lugar onde irá ser plotado, eixos, intervalo)
graficoCPU = animation.FuncAnimation(canvas, plotarGraficoCPU, fargs=(eixo_x_CPU, eixo_y_CPU), interval=1000)
graficoRAM = animation.FuncAnimation(canvas, plotarGraficoRAM, fargs=(eixo_x_RAM, eixo_y_RAM), interval=1000)
graficoDisco = animation.FuncAnimation(canvas, plotarGraficoDisco, fargs=(eixo_x_Disco, eixo_y_Disco), interval=1000)
plt.show()

