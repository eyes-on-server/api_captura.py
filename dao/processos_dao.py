
from database.conexao import criar_conexao_sql
producao = True


if producao == False:
    def inserir_processo(pid_processo, nome_processo, fk_servidor):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = ("INSERT INTO Eyes_On_Server.Processos(id_processos, pid_processos, nome_processos, fk_servidor"
                ") VALUES (null, %s, %s, %s);")

        values = [pid_processo, nome_processo, fk_servidor]

        comando.execute(query, values)
        conexao.commit()

        comando.close()
        conexao.close()
else:
    def inserir_processo(pid_processo, nome_processo, fk_servidor):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = ("INSERT INTO Processos( pid_processos, nome_processos, fk_servidor"
                ") VALUES ( ?, ?, ?);")

        values = (pid_processo, nome_processo, fk_servidor)

        comando.execute(query, values)
        conexao.commit()

        comando.close()
        conexao.close()
