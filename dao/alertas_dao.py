from database.conexao import criar_conexao


def inserir_alerta(fk_empresa, fk_servidor, fk_componente, titulo, desc, momento, tipo):

    conexao = criar_conexao()
    comando = conexao.cursor()

    query = ("INSERT INTO Eyes_On_Server.Alertas (fk_empresa, fk_servidor, fk_componente, titulo_alerta, "
             "descricao_alerta, data_hora_abertura, tipoAlerta) VALUES (%s, %s, %s, %s, %s, %s, %s);")
    valores = [fk_empresa, fk_servidor, fk_componente, titulo, desc, momento, tipo]

    comando.execute(query, valores)
    conexao.commit()

    comando.close()
    conexao.close()
