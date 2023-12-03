from database.conexao import criar_conexao_mysql
from database.conexao import criar_conexao_sql
producao = True


if producao == False:
    def consultar_servidor(mac_address):

        conexao = criar_conexao_mysql()
        comando = conexao.cursor()

        query = "SELECT * FROM Eyes_On_Server.Servidor WHERE mac_address = %s;"
        valores = [mac_address]

        comando.execute(query, valores)
        resultados = comando.fetchall()

        comando.close()
        conexao.close()

        return resultados


    def cadastrar_servidor(
            fk_empresa,
            nome_servidor,
            local_servidor,
            ipv6_servidor,
            mac_address,
            so_servidor,
            descricao
    ):

        conexao = criar_conexao_mysql()
        comando = conexao.cursor()

        query = "INSERT INTO Eyes_On_Server.Servidor VALUES (null, %s, %s, %s, %s, %s, %s, %s);"
        valores = [fk_empresa, nome_servidor, local_servidor, ipv6_servidor, mac_address, so_servidor, descricao]

        comando.execute(query, valores)
        conexao.commit()

        comando.close()
        conexao.close()
else: 
    def consultar_servidor(mac_address):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = "SELECT * FROM Servidor WHERE mac_address = ?;"
        valores = (mac_address)

        comando.execute(query, valores)
        resultados = comando.fetchall()

        comando.close()
        conexao.close()

        return resultados


    def cadastrar_servidor(
            fk_empresa,
            nome_servidor,
            local_servidor,
            ipv6_servidor,
            mac_address,
            so_servidor,
            descricao
    ):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = "INSERT INTO Servidor(fk_empresa, nome_servidor, local_servidor, ipv6_servidor, mac_address, so_servidor, descricao) VALUES ( ?, ?, ?, ?, ?, ?, ?);"
        valores = (fk_empresa, nome_servidor, local_servidor, ipv6_servidor, mac_address, so_servidor, descricao)

        comando.execute(query, valores)
        conexao.commit()

        comando.close()
        conexao.close()

