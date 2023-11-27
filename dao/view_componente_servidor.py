from database.conexao import criar_conexao_mysql


def consultar_componente_servidor(mac_address):

    conexao = criar_conexao_mysql()
    comando = conexao.cursor()

    query = "SELECT * FROM Eyes_On_Server.view_componentes_servidores WHERE `macAddress` = %s;"
    valores = [mac_address]

    comando.execute(query, valores)
    resultados = comando.fetchall()

    comando.close()
    conexao.close()

    return resultados


def coletar_id_componente_servidor(mac_address, tipo):

    conexao = criar_conexao_mysql()
    comando = conexao.cursor()

    query = ("SELECT `idComponenteServidor` FROM Eyes_On_Server.view_componentes_servidores WHERE `macAddress` = %s "
             "AND `Tipo` = %s;")
    valores = [mac_address, tipo]

    comando.execute(query, valores)
    resultados = comando.fetchall()

    comando.close()
    conexao.close()

    return resultados
