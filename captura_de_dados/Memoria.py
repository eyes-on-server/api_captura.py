import psutil as ps 
from acesso_banco.registro_dao import inserir_registro



class Memoria:

    def get_memory_usage(momento):
        
        memory_usage = (ps.virtual_memory().used * (10 ** -9))

        return memory_usage

    def get_memory_usage_percent(momento):
        
        memory_usage_percent = ps.virtual_memory().percent
        inserir_registro(4, 2, 2, memory_usage_percent, momento)

        return memory_usage_percent
