from database.conexao import criar_conexao_mysql
from database.conexao import criar_conexao_sql
producao = True


if producao == False:
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
else:
    def realizar_login(login, senha):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = "SELECT id_empresa, login, senha FROM View_Login WHERE login = ? AND senha = ?;"
        values = (login, senha)

        comando.execute(query, values)
        resultados = comando.fetchall()

        comando.close()
        conexao.close()

        return resultados

