from database.conexao import criar_conexao_mysql


def realizar_login(login, senha):

    conexao = criar_conexao_mysql()
    comando = conexao.cursor()

    query = "SELECT id_empresa, login, senha FROM Eyes_On_Server.View_Login WHERE login = %s AND senha = %s;"
    values = [login, senha]

    comando.execute(query, values)
    resultados = comando.fetchall()

    comando.close()
    conexao.close()

    return resultados


