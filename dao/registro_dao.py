from database.conexao import criar_conexao

conexao = criar_conexao()
comando = conexao.cursor()


def inserir_registro(fk_servidor, fk_componente, fk_medida, valor_registro, momento):

    query = ("INSERT INTO Eyes_On_Server.Registro(id_registro, fk_servidor, fk_componente, fk_medida, valor_registro, "
             "momento_registro) VALUES (null, %s, %s, %s, %s, %s);")

    values = [fk_servidor, fk_componente, fk_medida, valor_registro, momento]

    comando.execute(query, values)
    conexao.commit()

    comando.close()
    conexao.close()
