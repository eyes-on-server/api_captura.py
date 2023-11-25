from database.conexao import criar_conexao


def inserir_registro(fk_componente_servidor, valor_registro, momento):

    conexao = criar_conexao()
    comando = conexao.cursor()

    query = "INSERT INTO Eyes_On_Server.Registro VALUES (null, %s, %s, %s);"
    values = [fk_componente_servidor, valor_registro, momento]

    comando.execute(query, values)
    conexao.commit()

    comando.close()
    conexao.close()
