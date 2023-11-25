from database.conexao import criar_conexao


def consultar_componente_medida(tipo):

    conexao = criar_conexao()
    comando = conexao.cursor()

    query = "SELECT id_componente_medida FROM Eyes_On_Server.Componente_Medida where tipo = %s;"
    valores = [tipo]

    comando.execute(query, valores)
    resultados = comando.fetchall()

    comando.close()
    conexao.close()

    return resultados
