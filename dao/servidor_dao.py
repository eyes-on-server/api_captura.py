from database.conexao import criar_conexao

conexao = criar_conexao()
comando = conexao.cursor()


def consultar_servidor(mac_address):

    query = "SELECT * FROM Eyes_On_Server.Servidor WHERE mac_address = %s;"
    valores = [mac_address]

    comando.execute(query, valores)
    resultados = comando.fetchall()

    comando.close()
    conexao.close()

    return resultados
