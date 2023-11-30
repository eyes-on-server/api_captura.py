from enum import Enum

from captura_psutil.cpu.cpu_frequencia import CpuFrequencia
from captura_psutil.cpu.cpu_uso import CpuUso
from captura_psutil.cpu.cpu_temperatura import CpuTemperatura
from captura_psutil.disco.disco_uso import DiscoUso
from captura_psutil.memoria.memoria_uso import MemoriaUso
from captura_psutil.rede.rede_bytes_recebidos import RedeBytesRecebidos
from captura_psutil.rede.rede_bytes_enviados import RedeBytesEnviados


class ComponentesMonitorados(Enum):

    USO_PORCENTAGEM_CPU = {"nome": "Uso da CPU (%)", "metodo": CpuUso()}
    FREQUENCIA_CPU = {"nome": "Frequência da CPU (Htz)", "metodo": CpuFrequencia()}
    USO_MEMORIA_PORCENTAGEM = {"nome": "Uso da Memória (%)", "metodo": MemoriaUso()}
    USO_DISCO_PORCENTAGEM = {"nome": "Uso do Disco (%)", "metodo": DiscoUso()}
    BYTES_ENVIADOS_REDE = {"nome": "Bytes Enviados", "metodo": RedeBytesEnviados()}
    BYTES_RECEBIDOS_REDE = {"nome": "Bytes Recebidos", "metodo": RedeBytesRecebidos()}
    TEMPERATURA_CPU = {"nome": "Temperatura da Cpu (ºC)", "metodo": CpuTemperatura()}
