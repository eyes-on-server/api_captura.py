from database.conexao import criar_conexao_mysql


def inserir_downtime(fk_servidor, diferenca_segundos, prejuizo):

    conexao = criar_conexao_mysql()
    comando = conexao.cursor()

    query = "INSERT INTO Eyes_On_Server.Downtime VALUES (NULL, %s, %s, %s, now());"
    values = [fk_servidor, diferenca_segundos, prejuizo]

    comando.execute(query, values)
    conexao.commit()

    comando.close()
    conexao.close()
