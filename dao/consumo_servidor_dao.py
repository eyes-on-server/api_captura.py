from database.conexao import criar_conexao_mysql
from database.conexao import criar_conexao_sql
producao = True


if producao == False:
    def inserir_consumo_servidor(fk_servidor, porcentagem_uso):

        conexao = criar_conexao_mysql()
        comando = conexao.cursor()

        query = ("INSERT INTO Eyes_On_Server.Consumo_Servidor(id_consumo, fk_servidor, porcentagem_uso, momento"
                ") VALUES (NULL, %s, %s, now());")
        values = [fk_servidor, porcentagem_uso]

        comando.execute(query, values)
        conexao.commit()

        comando.close()
        conexao.close()
else:
    def inserir_consumo_servidor(fk_servidor, porcentagem_uso):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = ("INSERT INTO Consumo_Servidor( fk_servidor, porcentagem_uso, momento"
                ") VALUES ( ?, ?, GETDATE());")
        values = (fk_servidor, porcentagem_uso)

        comando.execute(query, values)
        conexao.commit()

        comando.close()
        conexao.close()