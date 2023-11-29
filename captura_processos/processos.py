import psutil as ps
from dao.processos_dao import inserir_processo
from time import sleep


def get_processos(id_servidor):

    for process in ps.process_iter():
        try:
            inserir_processo(process.pid, process.name(), id_servidor)

        except ps.NoSuchProcess:
            pass
