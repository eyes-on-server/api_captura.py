from database.conexao import executar


def inserir_processo(pid_processo, nome_processo, fk_servidor):
    query = ("INSERT INTO Eyes_On_Server.Processos(id_processos, pid_processos, nome_processos, fk_servidor"
             ") VALUES (null, %s, %s, %s);")

    values = [pid_processo, nome_processo, fk_servidor]

    executar(query, values)
