import os
import mysql.connector as mysql_con
import mysql.connector.errorcode
from dotenv import load_dotenv

load_dotenv()

producao = True
hostServer = os.environ.get('DB_HOST')
passwordServer = os.environ.get("DB_PASSWORD")
userServer = os.environ.get("DB_USER")
databaseServer = os.environ.get("DB_NAME")



if producao == False:
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
else:
    def criar_conexao_sql():
        try:
            conexao = pyodbc.connect('DRIVER={SQL SERVER}; SERVER=ec2-52-201-25-109.compute-1.amazonaws.com; DATABASE=Eyes_On_Server; UID=sa; PWD=Eyes_On_Server')  

            return conexao

        except mysql.connector.Error as error:
            print(f"Erro ao efetuar conexão >>> {error}")
