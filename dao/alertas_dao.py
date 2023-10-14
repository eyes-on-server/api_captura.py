from dao.connection import executar


def inserir_alerta(fk_empresa, fk_servidor, fk_componente, titulo, desc, momento, tipo):

    print('entrei no inserir alerta')

    query = ("INSERT INTO Eyes_On_Server.Alertas (fk_empresa, fk_servidor, fk_componente, titulo_alerta, "
             "descricao_alerta, data_hora_abertura, tipoAlerta) VALUES (%s, %s, %s, %s, %s, %s, %s);")
    valores = [fk_empresa, fk_servidor, fk_componente, titulo, desc, momento, tipo]

    executar(query, valores)
