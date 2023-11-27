import os
import mysql.connector as mysql_con
import mysql.connector.errorcode
from dotenv import load_dotenv

load_dotenv()

hostServer = os.environ.get('DB_HOST')
passwordServer = os.environ.get("DB_PASSWORD")
userServer = os.environ.get("DB_USER")
databaseServer = os.environ.get("DB_NAME")


def criar_conexao_mysql():
    try:
        conexao = mysql_con.connect(
            host=hostServer,
            password=passwordServer,
            user=userServer,
            database=databaseServer,
        )

        return conexao

    except mysql.connector.Error as error:
        print(f"Erro ao efetuar conexão >>> {error}")
