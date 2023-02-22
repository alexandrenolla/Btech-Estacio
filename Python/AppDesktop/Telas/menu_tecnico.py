# -*- coding: utf-8 -*-
from tkinter import *
import os
import sys
'''
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
janelaMenuTecnico = Tk()
janelaMenuTecnico.title('Ferramentaria')
janelaMenuTecnico.configure(background=corCinza)
janelaMenuTecnico.resizable(width=FALSE, height=FALSE)
janelaMenuTecnico.geometry("800x500")

# Título Cadastro técnico
frame_titulo = Frame(master=janelaMenuTecnico, width=800, height=60, bg=corBranca, relief=FLAT)
frame_titulo.place(x=0, y=20)
label_titulo = Label(master=frame_titulo, text="MENU TECNICO", bg=corBranca, fg=corLetra, font="Verdana 18 bold")
label_titulo.place(x=300, y=15)


def botao_consultar_ferramenta():
    os.system('python consulta_ferramenta.py')


# Botão Consultar Ferramenta
button_consultar_ferramenta_menu_tecnico = Button(janelaMenuTecnico, text='CONSULTAR FERRAMENTA', command=botao_consultar_ferramenta, font="Verdana 9 bold", highlightbackground=corBorda, fg=corLetra)
button_consultar_ferramenta_menu_tecnico.place(x=280, y=200, width=200, height=40)



# Impressão da tela
janelaMenuTecnico.mainloop()