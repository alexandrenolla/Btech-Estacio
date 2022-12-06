# Importando a biblioteca do BD
import sqlite3
from sqlite3 import Error

# Criando conexão com o banco de dos
def conexaoBanco():
    path = "/Users/mariacarolinaboabaid/Downloads/Python/inv_domestico/banco_dados.db"
    conexao = None
    try:
        conexao=sqlite3.connect(path)
        print("Conectado")
    except Error as ex:
        print(ex)
    return conexao

conectando = conexaoBanco()

# Inserindo dados no banco
    # Comando SQL INSERT 
comandoInserir = """INSERT INTO tb_inventario 
    (NOME, LOCAL, DESCRICAO, MARCA, DATA_COMPRA, VALOR_COMPRA, SERIE) 
    VALUES
    ("teste_nome", "teste_local", "teste_descricao", "teste_marca", "teste_data", "teste_valor", "teste_serie")"""
    # Função
def inserir (conexao, sql):
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        # Comando que grava os dados no SQLite
        conexao.commit()
        print("Registro inserido.")
    except Error as ex:
        print(ex)

# Deletando dados do banco:
    # Comando SQL DELETE
comandoDeletar = """DELETE FROM tb_inventario 
   WHERE ID=6"""
    # Função
def deletar (conexao, sql):
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        # Comando que grava os dados no SQLite
        conexao.commit()
        print("Registro deletado.")
    except Error as ex:
        print(ex)

# Atualizando dados no banco:
    # Comando SQL UPDATE
comandoAtualizar = """UPDATE tb_inventario SET NOME= 'Quadro', LOCAL='Quarto', DESCRICAO='Item decorativo', MARCA='Where Rich People Buy', DATA_COMPRA='23.03.2020', VALOR_COMPRA='12.500,00', SERIE='6777' WHERE ID=5"""
    # Função
def atualizar (conexao, sql):
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        # Comando que grava os dados no SQLite
        conexao.commit()
        print("Registro atualizado.")
    except Error as ex:
        print(ex)

# Selecionando e visualizando dados no banco
    # Comando SQL SELECT
comandoConsulta = """SELECT * FROM tb_inventario"""
    # Função
def consulta (conexao, sql):
    cur = conexao.cursor()
    cur.execute(sql)
    resultado = cur.fetchall()
    print("Registro consultado.")
    return resultado

# Selecionando e visualizando dado específico no banco
    # Comando SQL SELECT
comandoConsulta = """SELECT * FROM tb_inventario WHERE ID=4"""
    # Função
def consultaItemEspec (conexao, sql):
    cur = conexao.cursor()
    cur.execute(sql)
    resultado = cur.fetchall()
    print("Registro consultado.")
    return resultado

