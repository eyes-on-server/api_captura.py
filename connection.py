import os

import mysql.connector as sql
import mysql.connector.errorcode
from dotenv import load_dotenv

load_dotenv()



hostServer = os.environ.get('DB_HOST')
passwordServer = os.environ.get("DB_PASSWORD")
userServer = os.environ.get("DB_USER")
# portServer = int(os.environ.get("DB_PORT"))
databaseServer = os.environ.get("DB_NAME")

def executar(instrucao, valores):
    try:
        conexao = sql.connect(
            host=hostServer,
            password=passwordServer,
            user=userServer,
            port=3306,
            database=databaseServer,
        )

    except mysql.connector.Error as error:
        print(f"Erro ao efetuar conexão >>> {error}")
    comando = conexao.cursor()

    try:
        print(f"Executando comando: \n{instrucao}")
        if valores:
            comando.execute(instrucao, valores)
        conexao.commit()
    except mysql.connector.Error as erro:
        print("Erro ao executar comando!")
        print(erro)
    
    conexao.close()
