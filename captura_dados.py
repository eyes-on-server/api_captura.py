import datetime
import platform as plat
from time import sleep as s

import psutil as ps
from connection import executar
from message import mensagem_slack

osv = plat.uname().system
contador = 0
list_media_cpu = []
list_media_memoria = []
list_media_disco = []
media_geral_cpu = 0


def exibir_so():
    print(f"Seu sistema operacional é: {osv}")


dataAtual = datetime.datetime.now()
# os.system("clear")

# -=-=-=-=-=-=-=-=-=-= CPU -=-=-=-=-=-=-=-=-=-=


def exibir_dados_cpu():
    global media_geral_cpu
    global contador
    global list_media_cpu

    dict_cpu = {}
    list_cpu = []
    tempo_ocioso = ps.cpu_times().idle
    tempo_uso_kernel = ps.cpu_times().system

    qtd_cpus_virtuais = ps.cpu_count()
    qtd_cpus_fisicos = ps.cpu_count(logical=False)

    uso_cpus = ps.cpu_percent(interval=None, percpu=True)
    uso_cpu_geral = ps.cpu_percent(interval=None, percpu=False)
    media_geral_cpu = media_geral_cpu + uso_cpu_geral

    interrupcoes_cpu = ps.cpu_stats().interrupts

    frequencia_cpu_atual = ps.cpu_freq().current
    frequencia_cpu_max = ps.cpu_freq().max
    frequencia_cpu_min = ps.cpu_freq().min

    print(
        f"""
    ------------------ CPU --------------------- 
    Tempo Ocioso == {(tempo_ocioso/1000):.2f} s
    Tempo de Uso do Kernel == {(tempo_uso_kernel/1000):.2f} s
    Quantidade de CPUs Virtuais == {qtd_cpus_virtuais} -
    Quantidade de CPUs Fisicos == {qtd_cpus_fisicos} - 
    Uso geral da CPU == {uso_cpu_geral}"""
    )

    # % de Uso das CPUs == {dict_cpu}%
    for i in range(0, len(uso_cpus)):
        desc = "Porcentagem CPU " + str(i + 1)
        dict_cpu.clear()

        dict_cpu[f"Porcentagem CPU {(i + 1)}"] = uso_cpus[i]

        list_cpu.append(dict_cpu.copy())

        if contador == 0:
            list_media_cpu.append(uso_cpus[i])

        else:
            soma = uso_cpus[i]
            list_media_cpu[i] = list_media_cpu[i] + soma

        # executar(
        #    f"insert into Registro values (null, '{desc}', now(), {uso_cpus[i]}, 2, 3, 5);"
        # )

    print(
        f"""
    Tempo de interrupções da CPU == {(interrupcoes_cpu/1000000):.2f} s
    Frequência Atual da CPU == {(frequencia_cpu_atual/1000):.2f} GHz
    Frequência Máxima da CPU == {(frequencia_cpu_max/1000):.2f} GHz - 
    Frequência Mínima da CPU == {(frequencia_cpu_min/1000):.2f} GHz -
    """
    )
    if contador == 3:
        numero_cpu = 1
        print(
            f"Média geral de uso da CPU: {round(media_geral_cpu/ contador, 2)}")
        for i in list_media_cpu:
            media = i / contador
            print(f"Média de uso da CPU {numero_cpu}: {round(media,2)}%")
            numero_cpu = numero_cpu + 1

    executar(
        f"call RegistroCPU('{(tempo_ocioso/1000):.2f}', '{(tempo_uso_kernel/1000):.2f}', '{(interrupcoes_cpu/1000000):.2f}', '{(frequencia_cpu_atual/1000):.2f}')"
    )

    if uso_cpus[0] > 70:
        print(mensagem_slack("O uso da CPU está acima de 70%"))

    return {'uso': uso_cpu_geral, 'qtd_cpu': qtd_cpus_fisicos, 'qtd_vcpu': qtd_cpus_virtuais}

# -=-=-=-=-=-=-=-=-=-= Memória -=-=-=-=-=-=-=-=-=-=


def exibir_info_mem():

    memoria_usada = ps.virtual_memory().used
    memoria_total = ps.virtual_memory().total
    memoria_livre = ps.virtual_memory().free
    memoria_disponivel = ps.virtual_memory().available

    porcentagem_uso_memoria = round((memoria_usada * 100) / memoria_total, 2)
    list_media_memoria.append(porcentagem_uso_memoria)

    print(
        f"""
    ------------------ Memória --------------------- 
    Memória Total == {memoria_total/1000000000:.2f} GB -
    Memória Usada == {memoria_usada/1000000000:.2f} GB
    Memória Livre == {memoria_livre/1000000000:.2f} GB
    Memória Disponível == {memoria_disponivel/1000000000:.2f} GB
    """
    )
    if contador == 3:
        media_memoria = sum(list_media_memoria) / len(list_media_memoria)
        print(f"Média de uso de memoria: {round(media_memoria,2)}%")

    executar(
        f"call RegistroMemoria({memoria_usada/1000000000:.2f},  {memoria_livre/1000000000:.2f}, {memoria_disponivel/1000000000:.2f})"
    )

    if memoria_usada / (10**9) > 4:
        print(
            mensagem_slack(
                f"""O uso de memória ram é excessivo!
                                Data e hora do alerta: {dataAtual}"""
            )
        )

    return {'mem_total': f"{memoria_total/1000000000:.2f}GB", 'mem_livre': f"{memoria_livre/1000000000:.2f} GB", 'mem_usada': f"{memoria_usada/1000000000:.2f}GB", 'pct_uso': f"{porcentagem_uso_memoria}%"}

# -=-=-=-=-=-=-=-=-=-= Disco -=-=-=-=-=-=-=-=-=-=


def exibir_info_disco():

    dict_disk = {}
    list_disc = []
    print(f"""------------------ Disco ---------------------""")
    particoes_disco = ps.disk_partitions()
   
    uso_total_disco = ps.disk_usage(f"/").total
    disco_usado = ps.disk_usage(f"/").used
    disco_livre = ps.disk_usage(f"/").free
    porcent_disco = ps.disk_usage(f"/").percent
    list_media_disco.append(porcent_disco)

    dict_disk["Particao"] = particoes_disco[0].device
    dict_disk["Total"] = f"{(uso_total_disco/1000000000):.2f} GB"
    dict_disk["Usado"] = f"{(disco_usado/1000000000):.2f} GB"
    dict_disk["Livre"] = f"{(disco_livre/1000000000):.2f} GB"
    dict_disk["Porcentagem"] = f"{porcent_disco} %"

    list_disc.append(dict_disk.copy())
    print(dict_disk)
    if contador == 3:
        media_disco = sum(list_media_disco) / len(list_media_disco)
        print(f"Média de uso do disco: {round(media_disco,2)}%")
    executar(
        f"call RegistroDisco('{(uso_total_disco/1000000000):.2f}','{(disco_usado/1000000000):.2f}','{(disco_livre/1000000000):.2f}','{porcent_disco}')"
    )

    return {'disc_total': f"{(uso_total_disco/1000000000):.2f} GB", 'disc_usado': f"{(disco_usado/1000000000):.2f} GB", 'disc_livre': f"{(disco_livre/1000000000):.2f} GB", 'pct_uso': f"{porcent_disco}%"}

# -=-=-=-=-=-=-=-=-=-= Rede -=-=-=-=-=-=-=-=-=-=


def exibir_info_rede():

    bytes_enviados = ps.net_io_counters().bytes_sent
    bytes_recebidos = ps.net_io_counters().bytes_recv

    qtd_erros_entrada = ps.net_io_counters().errin
    qtd_erros_saida = ps.net_io_counters().errout

    # velocidade_rede_cabo = ps.net_if_stats()[0].speed
    # cabo_conectado = ps.net_if_stats()[0].isup

    print(
        f"""
    ------------------ Rede --------------------- 
    Bytes Enviados == {bytes_enviados/1000000:.2f} MB
    Bytes Recebidos == {bytes_recebidos/1000000:.2f} MB
    Quantidade de Erros na Entrada == {qtd_erros_entrada}
    Quantidade de Erros na Saida == {qtd_erros_saida}
    """
    )

    executar(
        f"call RegistroRede('{bytes_enviados/1000000:.2f}','{bytes_recebidos/1000000:.2f}','{qtd_erros_entrada}','{qtd_erros_saida}')"
    )

    return {'bytes_out': f"{bytes_enviados/1000000:.2f} MB/s", 'bytes_in': f"{bytes_recebidos/1000000:.2f} MB/s", 'qtd_erros_in': qtd_erros_entrada, 'qtd_erros_saida': qtd_erros_saida}


def exibir_info_temp():
    lista = []
    # -=-=-=-=-=-=-=-=-=-= Temperatura -=-=-=-=-=-=-=-=-=-=

    for i in range(0, len(ps.sensors_temperatures()["nvme"])):
        temperatura_cpu_label = ps.sensors_temperatures()["nvme"][i].label
        temperatura_cpu_atual = ps.sensors_temperatures()[
            "nvme"][i].current
        lista.append([f"{temperatura_cpu_label}°C",
                        f"{temperatura_cpu_atual}°C"])

    print(
        f"""
        ------------------ Temperatura --------------------- 
        Temperaturas do Entorno da CPU == {lista}
        """
    )
    executar(
        f"call RegistroTemperatura('{temperatura_cpu_label}','{temperatura_cpu_atual}')"
    )

    return {'cpu': f"{temperatura_cpu_atual}°C"}

