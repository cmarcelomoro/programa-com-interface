import streamlit as st
import pyodbc as pyodbc
import streamlit as st
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-H7OJ9TD\SQLEXPRESS;"
    "Database=Pessoas;"
    
)

def insere():

    nome = input("digite seu nome\n")
    idade = input("digite sua idade\n")
    email = input("digite seu email\n")
    queryInserir = "INSERT INTO pessoas VALUES('"+nome+"',"+idade+",'"+email+"')"
    cursor.execute(queryInserir)
    cursor.commit()
    cursor.close()
    return print("Inserção bem sucedida")

def selectAll():
    for row in cursor.execute("select * from pessoas"):
         print(row.id, row.nome, row.idade, row.email)


conexao = pyodbc.connect(dados_conexao)
print("conexao bem sucedida")

cursor =  conexao.cursor()


st.write(selectAll())
insere()
st.write("usando o write")
