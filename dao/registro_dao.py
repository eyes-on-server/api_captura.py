
from database.conexao import criar_conexao_sql
producao = True


if producao == False:
    def inserir_registro(fk_componente_servidor, valor_registro, momento):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = "INSERT INTO Eyes_On_Server.Registro VALUES (null, %s, %s, %s);"
        values = [fk_componente_servidor, valor_registro, momento]

        comando.execute(query, values)
        conexao.commit()

        comando.close()
        conexao.close()


    def ultimo_registro(fk_servidor):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = "SELECT MAX(Momento) FROM View_Registros WHERE Servidor = %s;"
        values = [fk_servidor]

        comando.execute(query, values)
        resultados = comando.fetchall()

        comando.close()
        conexao.close()

        return resultados


    def penultimo_registro(fk_servidor, ultimo_momento_registro):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = "SELECT MAX(Momento) FROM View_Registros WHERE Servidor = %s AND Momento < %s;"
        values = [fk_servidor, ultimo_momento_registro]

        comando.execute(query, values)
        resultados = comando.fetchall()

        comando.close()
        conexao.close()

        return resultados
else:
    def inserir_registro(fk_componente_servidor, valor_registro, momento):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = "INSERT INTO Registro(fk_componente_servidor, valor_registro, momento_registro) VALUES ( ?, ?, ?);"
        values = (fk_componente_servidor, valor_registro, momento)

        comando.execute(query, values)
        conexao.commit()

        comando.close()
        conexao.close()


    def ultimo_registro(fk_servidor):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = "SELECT MAX(Momento) FROM View_Registros WHERE Servidor = ?;"
        values = (fk_servidor)

        comando.execute(query, values)
        resultados = comando.fetchall()

        comando.close()
        conexao.close()

        return resultados


    def penultimo_registro(fk_servidor, ultimo_momento_registro):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = "SELECT MAX(Momento) FROM View_Registros WHERE Servidor = ? AND Momento < ?;"
        values = (fk_servidor, ultimo_momento_registro)

        comando.execute(query, values)
        resultados = comando.fetchall()

        comando.close()
        conexao.close()

        return resultados
