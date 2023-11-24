import os
import mysql.connector as sql
import mysql.connector.errorcode
from dotenv import load_dotenv

load_dotenv()

hostServer = os.environ.get('DB_HOST')
passwordServer = os.environ.get("DB_PASSWORD")
userServer = os.environ.get("DB_USER")
databaseServer = os.environ.get("DB_NAME")


def executar(instrucao, valores):

    global conexao
    global comando

    try:
        conexao = sql.connect(
            host=hostServer,
            password=passwordServer,
            user=userServer,
            database=databaseServer,
        )
        comando = conexao.cursor()

    except mysql.connector.Error as error:
        print(f"Erro ao efetuar conexão >>> {error}")

    try:
        print(f"""
            Comando >>> {instrucao}
            Valores >>> {valores}
        """)

        if valores:
            comando.execute(instrucao, valores)

        conexao.commit()

        comando.close()
        conexao.close()

    except mysql.connector.Error as erro:
        print("Erro ao executar comando!")
        print(erro)
