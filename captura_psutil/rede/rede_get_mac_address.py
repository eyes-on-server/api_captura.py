import psutil as ps
import os as so
from dao.servidor_dao import consultar_servidor

def validar_so():
    getSO = so.name
    global fk_servidor
 
    if getSO.startswith == 'e':
        fk_servidor = consultar_servidor(ps.net_if_addrs()['etho0'][0].address)[0][0]

    else:   
        fk_servidor = consultar_servidor(ps.net_if_addrs()['Ethernet'][0].address)[0][0]
       