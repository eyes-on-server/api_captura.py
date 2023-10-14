import psutil as ps
from dao.registro_dao import inserir_processo


class Processos:

    def get_processos(process_info):

        for process in ps.process_iter(["name", "pid"]):
            try:
                process_info = process.info
                #  print("Nome do processo: ", process_info['name'], "    |    PID do processo: ", process_info['pid'] )
                inserir_processo(process_info['pid'], process_info['name'], 4)
            
            except ps.NoSuchProcess:
                pass


    