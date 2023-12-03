from database.conexao import criar_conexao_mysql
from database.conexao import criar_conexao_sql
producao = True


if producao == False:
    
    def inserir_componente_servidor(fk_servidor, fk_componente_medida):

        conexao = criar_conexao_mysql()
        comando = conexao.cursor()

        query = "INSERT INTO Eyes_On_Server.Componente_Servidor VALUES (null, %s, %s);"
        valores = [fk_servidor, fk_componente_medida]

        comando.execute(query, valores)
        conexao.commit()

        comando.close()
        conexao.close()
else:
    def inserir_componente_servidor(fk_servidor, fk_componente_medida):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = "INSERT INTO Componente_Servidor(fk_servidor, fk_componente_medida) VALUES ( ?, ?);"
        valores = (fk_servidor, fk_componente_medida)

        comando.execute(query, valores)
        conexao.commit()

        comando.close()
        conexao.close()