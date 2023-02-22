# -*- coding: utf-8 -*-
from tkinter import *
import os
import sys
'''
Cadastrar tecnico
Cadastrar ferramenta
Consultar tecnico
Consultar ferramenta
'''

# Cores
corPreta = "#2e2d2b"
corBranca = "#feffff"
corVerde = "#8EB897"
corLetra = "#403d3d"
corCinza = "#e9edf5"
corBorda = "#82A0BC"

# Criando a janela
janelaMenuAdmin = Tk()
janelaMenuAdmin.title('Ferramentaria')
janelaMenuAdmin.configure(background=corCinza)
janelaMenuAdmin.resizable(width=FALSE, height=FALSE)
janelaMenuAdmin.geometry("800x500")

# Título Cadastro técnico
frame_titulo = Frame(master=janelaMenuAdmin, width=800, height=60, bg=corBranca, relief=FLAT)
frame_titulo.place(x=0, y=20)
label_titulo = Label(master=frame_titulo, text="MENU ADMIN", bg=corBranca, fg=corLetra, font="Verdana 18 bold")
label_titulo.place(x=300, y=15)

def botao_cadastrar_tecnico():
    os.system('python cadastro_tecnico.py')


def botao_consultar_tecnico():
    os.system('python consulta_tecnico_admin.py')


def botao_cadastrar_ferramenta():
    os.system('python cadastro_ferramenta.py')


def botao_consultar_ferramenta():
    os.system('python consulta_ferramenta_admin.py')


# Botão Cadastrar Tecnico
botao_cadastrar_tecnico_menu_admin = Button(janelaMenuAdmin, text='CADASTRAR TECNICO', command=botao_cadastrar_tecnico, font="Verdana 9 bold", highlightbackground=corVerde, fg=corLetra)
botao_cadastrar_tecnico_menu_admin.place(x=280, y=150, width=200, height=40)

# Botão Consultar Tecnico
botao_consultar_tecnico_menu_admin = Button(janelaMenuAdmin, text='CONSULTAR TECNICO', command=botao_consultar_tecnico, font="Verdana 9 bold", highlightbackground=corBorda, fg=corLetra)
botao_consultar_tecnico_menu_admin.place(x=280, y=220, width=200, height=40)

# Botão Cadastrar Ferramenta
botao_cadastrar_ferramenta_menu_admin = Button(janelaMenuAdmin, text='CADASTRAR FERRAMENTA', command=botao_cadastrar_ferramenta, font="Verdana 9 bold", highlightbackground=corVerde, fg=corLetra)
botao_cadastrar_ferramenta_menu_admin.place(x=280, y=290, width=200, height=40)
# Botão Consultar Ferramenta
botao_consultar_ferramenta_menu_admin = Button(janelaMenuAdmin, text='CONSULTAR FERRAMENTA', command=botao_consultar_ferramenta, font="Verdana 9 bold", highlightbackground=corBorda, fg=corLetra)
botao_consultar_ferramenta_menu_admin.place(x=280, y=360, width=200, height=40)

# Impressão da tela
janelaMenuAdmin.mainloop()