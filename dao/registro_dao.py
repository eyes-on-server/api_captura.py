from dao.connection import executar


def inserir_registro(fk_servidor, fk_componente, fk_medida, valor_registro, momento):

    query = ("INSERT INTO Eyes_On_Server.Registro(id_registro, fk_servidor, fk_componente, fk_medida, valor_registro, "
             "momento_registro) VALUES (null, %s, %s, %s, %s, %s);")

    values = [fk_servidor, fk_componente, fk_medida, valor_registro, momento]

    executar(query, values)

def inserir_processo(pid_processo, nome_processo, fk_servidor):

    query = ("INSERT INTO Eyes_On_Server.Processos(id_registro, pid_processos, nome_processos, fk_servidor, "
              ") VALUES (null, %s, %s, %s);")
    
    values = [pid_processo, nome_processo, fk_servidor]

    executar(query, values)
