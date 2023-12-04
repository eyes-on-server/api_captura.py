
from database.conexao import criar_conexao_sql
producao = True


if producao == False:
    
    def inserir_downtime(fk_servidor, diferenca_segundos, prejuizo):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = "INSERT INTO Eyes_On_Server.Downtime VALUES (NULL, %s, %s, %s, now());"
        values = [fk_servidor, diferenca_segundos, prejuizo]

        comando.execute(query, values)
        conexao.commit()

        comando.close()
        conexao.close()
else:
    def inserir_downtime(fk_servidor, diferenca_segundos, prejuizo):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = "INSERT INTO Downtime(fk_servidor, tempo_downtime, prejuizo, momento) VALUES ( ?, ?, ?, GETDATE());"
        values = (fk_servidor, diferenca_segundos, prejuizo)

        comando.execute(query, values)
        conexao.commit()

        comando.close()
        conexao.close()
