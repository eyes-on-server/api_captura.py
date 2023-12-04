
from database.conexao import criar_conexao_sql
producao = True


if producao == False:
    def inserir_alerta(fk_empresa, fk_servidor, fk_componente_medida, titulo, desc, momento, tipo):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = ("INSERT INTO Eyes_On_Server.Alertas (fk_empresa, fk_servidor, fk_componente_medida, titulo_alerta, "
                "descricao_alerta, data_hora_abertura, tipoAlerta) VALUES (%s, %s, %s, %s, %s, %s, %s);")
        valores = [fk_empresa, fk_servidor, fk_componente_medida, titulo, desc, momento, tipo]

        comando.execute(query, valores)
        conexao.commit()

        comando.close()
        conexao.close()
        
   
else: 
    def inserir_alerta(fk_empresa, fk_servidor, fk_componente_medida, titulo, desc, momento, tipo):

        conexao = criar_conexao_sql()
        comando = conexao.cursor()

        query = ("INSERT INTO Alertas (fk_empresa, fk_servidor, fk_componente_medida, titulo_alerta, "
                "descricao_alerta, data_hora_abertura, tipoAlerta) VALUES (?, ?, ?, ?, ?, ?, ?);")
        valores = (fk_empresa, fk_servidor, fk_componente_medida, titulo, desc, momento, tipo)

        comando.execute(query, valores)
        conexao.commit()

        comando.close()
        conexao.close()
