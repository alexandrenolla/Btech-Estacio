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

janelaMenuAdmin = Tk()

# Título da tela
janelaMenuAdmin.title('MENU')

# Tamanho da tela
janelaMenuAdmin.geometry("300x300")
janelaMenuAdmin.resizable(width=FALSE, height=FALSE)

def botao_cadastrar_tecnico():
    os.system('python cadastro_tecnico.py')


def botao_consultar_tecnico():
    os.system('python consulta_tecnico.py')


def botao_cadastrar_ferramenta():
    os.system('python cadastro_ferramenta.py')


def botao_consultar_ferramenta():
    os.system('python consulta_ferramenta.py')


# Botão Cadastrar Tecnico
botao_cadastrar_tecnico_menu_admin = Button(janelaMenuAdmin, text='Cadastrar Tecnico', command=botao_cadastrar_tecnico).place(x=50, y=20, width=200, height=40)

# Botão Consultar Tecnico
botao_consultar_tecnico_menu_admin = Button(janelaMenuAdmin, text='Consultar Tecnico', command=botao_consultar_tecnico).place(x=50, y=80, width=200, height=40)

# Botão Cadastrar Ferramenta
botao_cadastrar_ferramenta_menu_admin = Button(janelaMenuAdmin, text='Cadastrar Ferramenta', command=botao_cadastrar_ferramenta).place(x=50, y=180, width=200, height=40)

# Botão Consultar Ferramenta
botao_consultar_ferramenta_menu_admin = Button(janelaMenuAdmin, text='Consultar Ferramenta', command=botao_consultar_ferramenta).place(x=50, y=230, width=200, height=40)

# Impressão da tela
janelaMenuAdmin.mainloop()