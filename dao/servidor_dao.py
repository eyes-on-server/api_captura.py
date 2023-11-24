from database.conexao import executar


def consultar_servidor(macaddress):

    query = "SELECT * FROM Eyes_On_Server.Servidor WHERE mac_address = ?;"
    valores = [macaddress]

    return executar(query, valores)
