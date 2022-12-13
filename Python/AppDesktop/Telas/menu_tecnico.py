# -*- coding: utf-8 -*-
from tkinter import *
import os
import sys
'''
Consultar ferramenta
'''

janelaMenuTecnico = Tk()

# Título da tela
janelaMenuTecnico.title('MENU')

# Tamanho da tela
janelaMenuTecnico.geometry("300x300")
janelaMenuTecnico.resizable(width=FALSE, height=FALSE)


def botao_consultar_ferramenta():
    os.system('python consulta_ferramenta.py')


# Botão Consultar Ferramenta
button_consultar_ferramenta_menu_tecnico = Button(janelaMenuTecnico, text='Consultar Ferramenta', command=botao_consultar_ferramenta).place(x=50, y=100, width=200, height=40)



# Impressão da tela
janelaMenuTecnico.mainloop()