# EXECUTE ESSE ARQUIVO
# from time import sleep as s
# from captura_processos.Processos import Processos
# import datetime as dt
#
# processos = Processos()
#
#
# def start():
#
#     while True:
#
#         momento = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#
#         processos.get_processos()
#
#         s(5)


# start()

from enumerators.componentes_monitorados import ComponentesMonitorados
from dao.servidor_dao import consultar_servidor

for element in ComponentesMonitorados:
    print(element.value['nome'])

print(consultar_servidor("32423"))
