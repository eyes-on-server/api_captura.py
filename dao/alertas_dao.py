from dao.connection import executar


def inserir_alerta(fk_empresa, fk_servidor, fk_componente, titulo, desc, momento, tipo):

    query = "INSERT INTO Eyes_On_Server.Alertas VALUES (null, %s, %s, %s, %s, %s, %s, %s);"
    valores = [fk_empresa, fk_servidor, fk_componente, titulo, desc, momento, tipo]

    executar(query, valores)
