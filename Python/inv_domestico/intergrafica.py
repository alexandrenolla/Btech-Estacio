# Importes ---------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
import sqlite3
from sqlite3 import Error
from tkinter import messagebox

# BANCO DE DADOS ###################################################################################################################################################
# Criando conexão com o banco de dados
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
def inserir (conexao, tree):
    try:
        if entryID.get() != '':
            messagebox.showinfo(title="Error", message="O campo ID é automaticamente preenchido.\n Por gentileza, deixe o vazio.")
            entryID.delete(0, END)
            return
        elif entryNome.get() == '' or entryValor.get() == '':
            messagebox.showinfo(title="Error", message="O campo nome e valor são de preenchimento obrigatório.")
            return
        else:
            cur = conexao.cursor()
            # Criando as variáveis para inserir no comando SQL
            nomeDado = entryNome.get()
            localDado = entryLocal.get()
            descDado = entryDesc.get()
            marcaDado = entryMarca.get() 
            dataDado = entryData.get()
            valorDado = entryValor.get()
            serieDado = entrySerie.get()
            # Comando SQL
            cur.execute("""INSERT INTO tb_inventario 
            (NOME, LOCAL, DESCRICAO, MARCA, DATA_COMPRA, VALOR_COMPRA, SERIE) 
            VALUES
            (?, ?, ?, ?, ?, ?, ?)""", (nomeDado, localDado, descDado, marcaDado, dataDado, valorDado, serieDado))
            # Comando que grava os dados no SQLite
            conexao.commit()
            # Inserindo os dados na TreeView
            cur.execute("""SELECT * FROM tb_inventario""")
            resultado_ID = cur.fetchall()
            tree.insert("", "end", values=(resultado_ID[len(resultado_ID) - 1][0], entryNome.get(), entryLocal.get(), entryDesc.get(), entryMarca.get(), entryData.get(), entryValor.get(), entrySerie.get()))
            # Deletando as informações do campo
            entryNome.delete(0, END)
            entryLocal.delete(0, END)
            entryDesc.delete(0, END)
            entryMarca.delete(0, END) 
            entryData.delete(0, END)
            entryValor.delete(0, END)
            entrySerie.delete(0, END)  
    except Error as ex:
        print(ex)

# Deletando dados do banco:
def deletar (conexao, tree):
    try:
        # Caso o usuário não indique o ID do item para deleter
        if entryID.get() == '':
            messagebox.showinfo(title="Error", message="O campo ID é de preenchimento obrigatório.")
            return
        else:
            cur = conexao.cursor()
            # Colocando o ID em uma variável
            idDelete = entryID.get()
            # Comando SQL delete
            cur.execute("""DELETE FROM tb_inventario 
            WHERE ID=?""", [idDelete])
            # Deletando as informações do campo
            entryID.delete(0, END)
            entryNome.delete(0, END)
            entryLocal.delete(0, END)
            entryDesc.delete(0, END)
            entryMarca.delete(0, END) 
            entryData.delete(0, END)
            entryValor.delete(0, END)
            entrySerie.delete(0, END)
            # Mensagem de sucesso
            messagebox.showinfo(title="Informação", message="Item deletado com sucesso!")
            # Comando que grava os dados no SQLite
            conexao.commit()
            # Removendo todos os itens da Treeview
            for i in tree.get_children():
                tree.delete(i)
            # Atualizando itens da treeview conforme banco de dados 
            cur.execute("""SELECT * FROM tb_inventario""")
            resultado = cur.fetchall()
            for row in resultado:
                tree.insert("", "end", values=row)
    except Error as ex:
        print(ex)

# Atualizando dados no banco:
def atualizar (conexao, tree):
    try:
        cur = conexao.cursor()
        if entryID.get() == '':
            messagebox.showinfo(title="Error", message="O campo ID é de preenchimento obrigatório.")
        else: 
            updateID = entryID.get()
            if entryNome.get() != '':
                novoNome = entryNome.get()
                cur.execute("""UPDATE tb_inventario SET NOME= ? WHERE ID=?""", (novoNome, updateID))

            if entryLocal.get() != '':
                novoLocal = entryLocal.get()
                cur.execute("""UPDATE tb_inventario SET LOCAL= ? WHERE ID=?""", (novoLocal, updateID))

            if entryDesc.get() != '':
                novoDesc = entryDesc.get()
                cur.execute("""UPDATE tb_inventario SET DESCRICAO ? WHERE ID=?""", (novoDesc, updateID))

            if entryMarca.get() != '':
                novoMarca = entryMarca.get()
                cur.execute("""UPDATE tb_inventario SET MARCA= ? WHERE ID=?""", (novoMarca, updateID))

            if entryData.get() != '':
                novoData = entryData.get()
                cur.execute("""UPDATE tb_inventario SET DATA_COMORA= ? WHERE ID=?""", (novoMarca, updateID))
            
            if entryValor.get() != '':
                novoValor= entryValor.get()
                cur.execute("""UPDATE tb_inventario SET VALOR_COMPRA= ? WHERE ID=?""", (novoValor, updateID))
            
            if entrySerie.get() != '':
                novoSerie = entrySerie.get()
                cur.execute("""UPDATE tb_inventario SET SERIE= ? WHERE ID=?""", (novoSerie, updateID))
        # Comando que grava os dados no SQLite
        conexao.commit()
        # Deletando as informações do campo
        entryID.delete(0, END)
        entryNome.delete(0, END)
        entryLocal.delete(0, END)
        entryDesc.delete(0, END)
        entryMarca.delete(0, END) 
        entryValor.delete(0, END)
        entrySerie.delete(0, END)
        # Removendo todos os itens da Treeview
        for i in tree.get_children():
            tree.delete(i)
            # Atualizando itens da treeview conforme banco de dados 
        cur.execute("""SELECT * FROM tb_inventario""")
        resultado = cur.fetchall()
        for row in resultado:
            tree.insert("", "end", values=row)
    except Error as ex:
        print(ex)

# Selecionando todos os itens no banco para visualizar:
def consulta (conexao, tree):
    cur = conexao.cursor()
    cur.execute("""SELECT * FROM tb_inventario""")
    resultado = cur.fetchall()
    # Removendo todos os itens da Treeview
    for i in tree.get_children():
            tree.delete(i)
    for row in resultado:
        tree.insert("", "end", values=row)
    return resultado

# Selecionando e visualizando dado específico no banco
def consultaItemEspec (conexao, tree):
    # Caso o usuário não indique o ID do item para deleter
    if entryID.get() == '':
        messagebox.showinfo(title="Error", message="O campo ID é de preenchimento obrigatório.")
        return
    else:
        cur = conexao.cursor()
        # Colocando o ID em uma variável
        idVisualizar = entryID.get()
        cur.execute("""SELECT * FROM tb_inventario WHERE ID=?""", [idVisualizar])
        # Removendo todos os itens da Treeview
        for i in tree.get_children():
            tree.delete(i)
        # Deletando as informações do campo
            entryID.delete(0, END)
            entryNome.delete(0, END)
            entryLocal.delete(0, END)
            entryDesc.delete(0, END)
            entryMarca.delete(0, END) 
            entryValor.delete(0, END)
            entrySerie.delete(0, END)
        # Selecionando o item
        resultado = cur.fetchall()
        for row in range(0, len(resultado)):
            if resultado[row][0] == int(idVisualizar):
                tree.insert("", "end", values=resultado[row])


# TKINTER - INTERFACE GRÁFICA ######################################################################################################################################
# Cores ------------------------------------------------------------------------------------------------------------------------------------------------------------
corPreta = "#2e2d2b" 
corBranca = "#feffff" 
corVerde1 = "#4fa882" 
corValor = "#38576b"
corLetra = "#403d3d" 
corProfit = "#e06636" 
corAzul = "#038cfc" 
corVerde2 = "#3fbfb9"
corCinza = "#e9edf5" 
corBorda ="#82A0BC" 

# Criando janela ---------------------------------------------------------------------------------------------------------------------------------------------------
janela = Tk()
janela.title("Inventário Doméstico")
janela.configure(background=corCinza)
    # Bloqueando a opção do Usuário de alterar o tamanho da janela
janela.resizable(width=FALSE, height=FALSE)
    # Largura x Altura
janela.geometry("1100x600")
    # Configuração de style
style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames ---------------------------------------------------------------------------------------------------------------------------------------------------
frameTitulo = Frame(master=janela, width=1100, height=62, bg=corCinza, relief=FLAT)
frameTitulo.place(x=0, y=0)

frameContainerWidgets = Frame(master=janela, width=1043, height=303, bg=corCinza, relief=FLAT)
frameContainerWidgets.place(x=0, y=65)

frameDados = Frame(master=janela, width=1300, height=200, bg=corBranca, relief=FLAT)
frameDados.place(x=0, y=380)

# Logo -------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Acessando o logo
appLogo = Image.open("logo.png")
    # Alterando o tamanho do logo
appLogo = appLogo.resize((45,45))
appLogo = ImageTk.PhotoImage(appLogo) 
    # Criando a label para inserir o logo e o título
appLogoLabel = Label(master=frameTitulo, image=appLogo, text=" Inventário Doméstico", height=53, width=1100, compound=LEFT, relief=RAISED, anchor=NW, bg=corBranca, font=("Verdana 20 bold"), fg=corPreta)
appLogoLabel.place(x=0, y=4)

# Entradas ---------------------------------------------------------------------------------------------------------------------------------------------------------
    # ID
l_id = Label(master=frameContainerWidgets, text="ID", bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
l_id.place(x=20, y=20)
entryID = Entry(master=frameContainerWidgets, bg=corBranca, fg=corLetra, justify="left", width= 30, font=("Verdana 11 italic"), relief=RAISED, borderwidth=0, highlightbackground=corBorda)
entryID.place(x=150, y=21)  

    # Nome
nome = Label(master=frameContainerWidgets, text="Nome", bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
nome.place(x=20, y=50)  
entryNome = Entry(master=frameContainerWidgets, bg=corBranca, fg=corLetra, justify="left", width= 30, font=("Verdana 11 italic"), relief=RAISED, borderwidth=0, highlightbackground=corBorda)
entryNome.place(x=150, y=51)  

    # Local
local = Label(master=frameContainerWidgets, text="Local", bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
local.place(x=20, y=80)  
entryLocal = Entry(master=frameContainerWidgets, bg=corBranca, fg=corLetra, justify="left", width= 30, font=("Verdana 11 italic"), relief=RAISED, borderwidth=0,  highlightbackground=corBorda)
entryLocal.place(x=150, y=81)  

    # Descrição
descricao = Label(master=frameContainerWidgets, text="Descrição", bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
descricao.place(x=20, y=110)  
entryDesc = Entry(master=frameContainerWidgets, bg=corBranca, fg=corLetra, justify="left", width= 30, font=("Verdana 11 italic"), relief=RAISED, borderwidth=0,  highlightbackground=corBorda)
entryDesc.place(x=150, y=111)  

    # Marca
marca = Label(master=frameContainerWidgets, text="Marca", bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
marca.place(x=20, y=140)  
entryMarca = Entry(master=frameContainerWidgets, bg=corBranca, fg=corLetra, justify="left", width= 30, font=("Verdana 11 italic"), relief=RAISED, borderwidth=0,  highlightbackground=corBorda)
entryMarca.place(x=150, y=141) 

    # Data da compra
data = Label(master=frameContainerWidgets, text="Data da Compra", bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
data.place(x=20, y=170)
entryData = DateEntry(master=frameContainerWidgets, width= 10, font=("Verdana 11"), background="darkblue", borderwidth=0,  highlightbackground=corBorda)
entryData.place(x=150, y=171)

    # Valor da compra 
valor = Label(master=frameContainerWidgets, text="Valor da Compra", bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
valor.place(x=20, y=200)  
entryValor = Entry(master=frameContainerWidgets, bg=corBranca, fg=corLetra, justify="left", width= 30, font=("Verdana 11 italic"), relief=RAISED, borderwidth=0, highlightbackground=corBorda)
entryValor.place(x=150, y=201) 

    # Série
serie = Label(master=frameContainerWidgets, text="Número de Série", bg=corCinza, fg=corLetra, font=("Verdana 12 bold"))
serie.place(x=20, y=230)  
entrySerie = Entry(master=frameContainerWidgets, bg=corBranca, fg=corLetra, justify="left", width= 30, font=("Verdana 11 italic"), relief=RAISED, borderwidth=0, highlightbackground=corBorda)
entrySerie.place(x=150, y=231) 
# Adicionando vertical scrollbar na tabela de dados ----------------------------------------------------------------------------------------------------------------
vertical_scroll = ttk.Scrollbar(master=frameDados)
vertical_scroll.pack(side=RIGHT, fill=Y)

# Criando a tabela de dados ----------------------------------------------------------------------------------------------------------------------------------------
lista_itens = []
global tabela_dados
itens_head = ["id", "nome", "local", "descricao", "marca", "data_compra", "valor_compra", "serie"]

tabela_dados = ttk.Treeview(master=frameDados, 
columns=itens_head, show="headings", height=5, yscrollcommand=vertical_scroll.set, selectmode="extended")
style.configure("Treeview", rowheight=31)

    # Configurando o tamanho das colunas
tabela_dados.column("id", minwidth=1, width=50)
tabela_dados.column("nome", minwidth=1, width=130)
tabela_dados.column("local", minwidth=1, width=120)
tabela_dados.column("descricao", minwidth=1, width=190)
tabela_dados.column("marca", minwidth=1, width=170)
tabela_dados.column("data_compra", minwidth=1, width=140)
tabela_dados.column("valor_compra", minwidth=1, width=135)
tabela_dados.column("serie", minwidth=1, width=120)

    # Configurando o heading das colunas
tabela_dados.heading("id", text="ID")
tabela_dados.heading("nome", text="Nome")
tabela_dados.heading("local", text="Local")
tabela_dados.heading("descricao", text="Descrição")
tabela_dados.heading("marca", text="Marca")
tabela_dados.heading("data_compra", text="Data da Compra")
tabela_dados.heading("valor_compra", text="Valor da Compra")
tabela_dados.heading("serie", text="Série")

    # Inserindo dados do banco no Treeview
cur = conectando.cursor()
cur.execute("""SELECT * FROM tb_inventario""")
resultado = cur.fetchall()
for row in resultado:
        tabela_dados.insert("", "end", values=row)

tabela_dados.pack(padx=10)

# Configurando o vertical scrollbar --------------------------------------------------------------------------------------------------------------------------------
vertical_scroll.config(command=tabela_dados.yview)

# Botões CRUD ------------------------------------------------------------------------------------------------------------------------------------------------------
    # Adicionar
b_adicionar = Button(master=frameContainerWidgets, command=lambda: inserir(conectando, tabela_dados), compound=LEFT,  text="ADICIONAR", font=("Verdana 10 bold"), highlightbackground=corCinza, anchor=CENTER, overrelief=RIDGE, fg=corVerde1, height=2, width=10)
b_adicionar.place(x=420, y=21)

    # Atualizar
b_atualizar = Button(master=frameContainerWidgets, command=lambda: atualizar(conectando, tabela_dados), compound=LEFT, text="ATUALIZAR", font=("Verdana 10 bold"), highlightbackground=corCinza, anchor=CENTER, overrelief=RIDGE, fg=corAzul, height=2, width=10)
b_atualizar.place(x=420, y=71)

    # Deletar
b_deletar = Button(master=frameContainerWidgets,command=lambda: deletar(conectando, tabela_dados),compound=LEFT, text="DELETAR", font=("Verdana 10 bold"), highlightbackground=corCinza, anchor=CENTER, overrelief=RIDGE, fg=corProfit, height=2, width=10)
b_deletar.place(x=420, y=121)

    # Visualizar
b_visualizar = Button(master=frameContainerWidgets, command=lambda: consultaItemEspec(conectando, tabela_dados), compound=LEFT, text="VISUALIZAR ITEM SELECIONADO POR ID", font=("Verdana 10 bold"), highlightbackground=corCinza, anchor=CENTER, overrelief=RIDGE, fg=corVerde2, height=2, width=32)
b_visualizar.place(x=660, y=80)

b_visualizarTodos= Button(master=frameContainerWidgets, command=lambda: consulta(conectando, tabela_dados), compound=LEFT, text="VISUALIZAR TODOS OS ITENS", font=("Verdana 10 bold"), highlightbackground=corCinza, anchor=CENTER, overrelief=RIDGE, fg=corVerde2, height=2, width=25)
b_visualizarTodos.place(x=685, y=140)

# Abrir janela -----------------------------------------------------------------------------------------------------------------------------------------------------
janela.mainloop()


