# -*- coding: utf-8 -*-
# IMPORTES
# import sqlite3
# from bancos import bancoUsuarios, curUsuarios
# from bancos import bancoTecnicos, curTecnicos
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import messagebox


# Limitação de 40 caracteres para o campo do nome
def limitar_caractere_nome(p):
    if len(p) > 40:
        return False
    return True


# Limitação de 11 caracteres para o campo do cpf
def limitar_caractere_cpf(p):
    if len(p) > 11:
        return False
    return True


# Limitação de 9 caracteres para o campo do telefone
def limitar_caractere_telefone(p):
    if len(p) > 9:
        return False
    return True


# Limitação de 30 caracteres para o campo do telefone
def limitar_caractere_equipe(p):
    if len(p) > 30:
        return False
    return True


# Limitação de valores apenas numéricos nos campos de cpf e telefone
def botao_cadastrar():
    try:
        int(entry_cpf_tecnico.get())
        int(entry_telefone_tecnico.get())
        messagebox.showinfo(title="Sucesso", message="O Tecnico foi cadastrado.")
        # Limpeza dos campos após confirmação de cadastro
        entry_nome_tecnico.delete(0, END)
        entry_cpf_tecnico.delete(0, END)
        entry_telefone_tecnico.delete(0, END)
        entry_nome_equipe.delete(0, END)
    except ValueError:
        messagebox.showinfo(title="Erro", message="Os campos do CPF e do Telefone são exclusivamente númericos.")


def botao_cancelar():
   janelaCadastroTecnico.destroy()


# Cores
corPreta = "#2e2d2b"
corBranca = "#feffff"
corVerde = "#8EB897"
corLetra = "#403d3d"
corCinza = "#e9edf5"
corBorda = "#82A0BC"

# Criando a janela
janelaCadastroTecnico = Tk()
janelaCadastroTecnico.title('Ferramentaria')
janelaCadastroTecnico.configure(background=corCinza)
janelaCadastroTecnico.resizable(width=FALSE, height=FALSE)
janelaCadastroTecnico.geometry("800x480")

# Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_nome = janelaCadastroTecnico.register(func=limitar_caractere_nome)

# Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_cpf = janelaCadastroTecnico.register(func=limitar_caractere_cpf)

# Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_telefone = janelaCadastroTecnico.register(func=limitar_caractere_telefone)

# Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_equipe = janelaCadastroTecnico.register(func=limitar_caractere_equipe)

# Título Cadastro técnico
frame_titulo = Frame(master=janelaCadastroTecnico, width=800, height=60, bg=corBranca, relief=FLAT)
frame_titulo.place(x=0, y=20)
label_titulo = Label(master=frame_titulo, text="CADASTRAR TÉCNICO", bg=corBranca, fg=corLetra, font="Verdana 18 bold")
label_titulo.place(x=300, y=15)

# Campo do Nome
label_nome_tecnico = Label(text='NOME COMPLETO', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_nome_tecnico.place(x=170, y=120)
entry_nome_tecnico = Entry(janelaCadastroTecnico, validate='key', validatecommand=(vcmd_nome, '%P'), font="Verdana 9 bold", bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=45)
entry_nome_tecnico.place(x=300, y=120)

# Campo do CPF
label_cpf_tecnico = Label(text='CPF', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_cpf_tecnico.place(x=170, y=160)
entry_cpf_tecnico = Entry(janelaCadastroTecnico, validate='key', validatecommand=(vcmd_cpf, '%P'), font="Verdana 9 bold", bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=45)
entry_cpf_tecnico.place(x=300, y=160)

# Campo do Telefone
label_telefone_tecnico = Label(text='TELEFONE', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_telefone_tecnico.place(x=170, y=200)
entry_telefone_tecnico = Entry(janelaCadastroTecnico, validate='key', validatecommand=(vcmd_telefone, '%P'), font="Verdana 9 bold", bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=45)
entry_telefone_tecnico.place(x=300, y=200)

# Campo do Nome da equipe
label_nome_equipe = Label(text='EQUIPE', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_nome_equipe.place(x=170, y=240)
entry_nome_equipe = Entry(janelaCadastroTecnico, validate='key', validatecommand=(vcmd_equipe, '%P'), font="Verdana 9 bold", bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=45)
entry_nome_equipe.place(x=300, y=240)

# Campo Turno
lista_turno = ['MATUTINO', 'VESPERTINO', 'NOTURNO']
turno = Label(text='TURNO', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
turno.place(x=170, y=280)
combobox_turno = Combobox(values=lista_turno)
combobox_turno.place(x=300, y=280) 
style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground=corBranca, background=corBranca)

# Campo Validação Adminstrador
admin = BooleanVar()
admin.set(False)
checkbutton_admin = Checkbutton(janelaCadastroTecnico, text='  ADMINISTRADOR', variable=admin, bg=corCinza, fg=corLetra, font="Verdana 10 bold")
checkbutton_admin.place(x=300, y=320) 

# Campo Senha
label_senha_cadastro = Label(master=janelaCadastroTecnico, text="SENHA", bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_senha_cadastro.place(x=170, y=360)
entry_senha_cadastro = Entry(master=janelaCadastroTecnico, bg=corBranca, fg=corLetra, justify="left", width=40, font="Verdana 12", borderwidth=0, highlightbackground=corBorda)
entry_senha_cadastro.place(x=300, y=360)

# Botão Cancelar
botao_cancelar_tecnico = Button(master=janelaCadastroTecnico, text="CANCELAR", font="Verdana 9 bold", highlightbackground=corBorda, fg=corLetra,  height=2, width=15, command=botao_cancelar)
botao_cancelar_tecnico.place(x=300, y=420)

# Botão Cadastrar
botao_cadastrar_tecnico = Button(master=janelaCadastroTecnico, text="CADASTRAR", font="Verdana 9 bold", highlightbackground=corVerde, fg=corLetra, height=2, width=15, command=botao_cadastrar)
botao_cadastrar_tecnico.place(x=485, y=420)

            
# Impressão da tela
janelaCadastroTecnico.mainloop()
