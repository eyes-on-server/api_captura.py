from database.conexao import criar_conexao_mysql


def inserir_registro(fk_componente_servidor, valor_registro, momento):

    conexao = criar_conexao_mysql()
    comando = conexao.cursor()

    query = "INSERT INTO Eyes_On_Server.Registro VALUES (null, %s, %s, %s);"
    values = [fk_componente_servidor, valor_registro, momento]

    comando.execute(query, values)
    conexao.commit()

    comando.close()
    conexao.close()


def ultimo_registro(fk_servidor):

    conexao = criar_conexao_mysql()
    comando = conexao.cursor()

    query = "SELECT MAX(Momento) FROM View_Registros WHERE Servidor = %s;"
    values = [fk_servidor]

    comando.execute(query, values)
    resultados = comando.fetchall()

    comando.close()
    conexao.close()

    return resultados


def penultimo_registro(fk_servidor, ultimo_momento_registro):

    conexao = criar_conexao_mysql()
    comando = conexao.cursor()

    query = "SELECT MAX(Momento) FROM View_Registros WHERE Servidor = %s AND Momento < %s;"
    values = [fk_servidor, ultimo_momento_registro]

    comando.execute(query, values)
    resultados = comando.fetchall()

    comando.close()
    conexao.close()

    return resultados
