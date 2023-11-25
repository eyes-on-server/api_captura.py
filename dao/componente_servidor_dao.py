from database.conexao import criar_conexao


def inserir_componente_servidor(fk_servidor, fk_componente_medida):

    conexao = criar_conexao()
    comando = conexao.cursor()

    query = "INSERT INTO Eyes_On_Server.Componente_Servidor VALUES (null, %s, %s);"
    valores = [fk_servidor, fk_componente_medida]

    comando.execute(query, valores)
    conexao.commit()

    comando.close()
    conexao.close()
