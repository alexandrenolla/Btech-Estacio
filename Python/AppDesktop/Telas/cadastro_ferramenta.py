# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import os
import sys
# from tkinter.ttk import Combobox


# Limitação de 60 caracteres para o campo da descrição
def limitar_caractere_descricao(p):
    if len(p) > 60:
        return False
    return True


# Limitação de 25 caracteres para o campo do part number
def limitar_caractere_number(p):
    if len(p) > 25:
        return False
    return True


# Limitação de 30 caracteres para o campo do fabricante
def limitar_caractere_fabricante(p):
    if len(p) > 30:
        return False
    return True


# Limitação de 15 caracteres para o campo da voltagem
def limitar_caractere_voltagem(p):
    if len(p) > 15:
        return False
    return True


# Limitação de 20 caracteres para o campo do tamanho
def limitar_caratere_tamanho(p):
    if len(p) > 20:
        return False
    return True


# Limitação de 15 caracteres para o campo da medida
def limitar_caratere_medida(p):
    if len(p) > 15:
        return False
    return True


# Limitação de 15 caracteres para o campo do tipo
def limitar_caratere_tipo(p):
    if len(p) > 15:
        return False
    return True


# Limitação de 15 caracteres para o campo do material
def limitar_caratere_material(p):
    if len(p) > 15:
        return False
    return True


# Limitação de valores apenas numéricos nos campos de tamanho e part number
def botao_cadastrar():
    try:
        int(entry_number_cadastro_ferramenta.get())
        int(entry_tamanho_cadastro_ferramenta.get())
        messagebox.showinfo(title="Sucesso", message="A ferramenta foi cadastrada.")
        # Limpeza dos campos após confirmação de cadastro
        entry_descricao_cadastro_ferramenta.delete(0, END)
        entry_number_cadastro_ferramenta.delete(0, END)
        entry_fabricante_cadastro_ferramenta.delete(0, END)
        entry_voltagem_cadastro_ferramenta.delete(0, END)
        entry_tamanho_cadastro_ferramenta.delete(0, END)
        entry_medida_cadastro_ferramenta.delete(0, END)
        entry_tipo_cadastro_ferramenta.delete(0, END)
        entry_material_cadastro_ferramenta.delete(0, END)
    except ValueError:
        messagebox.showinfo(title="Erro", message="Os campos do Part Number e do Tamanho são exclusivamente númericos.")


def botao_cancelar():
    janelaCadastroFerramenta.destroy()

# Cores
corPreta = "#2e2d2b"
corBranca = "#feffff"
corVerde = "#8EB897"
corLetra = "#403d3d"
corCinza = "#e9edf5"
corBorda = "#82A0BC"

# Criando a janela
janelaCadastroFerramenta = Tk()
janelaCadastroFerramenta.title('Ferramentaria')
janelaCadastroFerramenta.configure(background=corCinza)
janelaCadastroFerramenta.resizable(width=FALSE, height=FALSE)
janelaCadastroFerramenta.geometry("800x500")

# Título Cadastro técnico
frame_titulo = Frame(master=janelaCadastroFerramenta, width=800, height=60, bg=corBranca, relief=FLAT)
frame_titulo.place(x=0, y=20)
label_titulo = Label(master=frame_titulo, text="CADASTRAR FERRAMENTA", bg=corBranca, fg=corLetra, font="Verdana 18 bold")
label_titulo.place(x=300, y=15)

# Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_descricao = janelaCadastroFerramenta.register(func=limitar_caractere_descricao)

# Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_number = janelaCadastroFerramenta.register(func=limitar_caractere_number)

# Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_voltagem = janelaCadastroFerramenta.register(func=limitar_caractere_voltagem)

# Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_fabricante = janelaCadastroFerramenta.register(func=limitar_caractere_fabricante)

# Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_tamanho = janelaCadastroFerramenta.register(func=limitar_caratere_tamanho)

# Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_medida = janelaCadastroFerramenta.register(func=limitar_caratere_medida)

# Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_tipo = janelaCadastroFerramenta.register(func=limitar_caratere_tipo)

# Atribuindo a função a uma variável que servirá de parâmetro para o método de validação
vcmd_material = janelaCadastroFerramenta.register(func=limitar_caratere_material)

# Campo da Descrição da janela
label_descricao_cadastro_ferramenta = Label(text='DESCRIÇÃO', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_descricao_cadastro_ferramenta.place(x=140, y=120)
entry_descricao_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_descricao, '%P'), font="Verdana 9 bold", bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=45)
entry_descricao_cadastro_ferramenta.place(x=300, y=120)

# Campo do Part Number da ferramenta
label_number_cadastro_ferramenta = Label(text='PART NUMBER', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_number_cadastro_ferramenta.place(x=140, y=160)
entry_number_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_number, '%P'), font="Verdana 9 bold", bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=45)
entry_number_cadastro_ferramenta.place(x=300, y=160)

# Campo do Fabricante da ferramenta
label_fabricante_cadastro_ferramenta = Label(text='FABRICANTE', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_fabricante_cadastro_ferramenta.place(x=140, y=200)
entry_fabricante_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_fabricante, '%P'), font="Verdana 9 bold", bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=45)
entry_fabricante_cadastro_ferramenta.place(x=300, y=200)

# Campo da Voltagem da ferramenta
label_voltagem_cadastro_ferramenta = Label(text='VOLTAGEM', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_voltagem_cadastro_ferramenta.place(x=140, y=240)
entry_voltagem_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_voltagem, '%P'), font="Verdana 9 bold", bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=45)
entry_voltagem_cadastro_ferramenta.place(x=300, y=240)

# Campo do Tamanho da ferramenta
label_tamanho_cadastro_ferramenta = Label(text='TAMANHO', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_tamanho_cadastro_ferramenta.place(x=140, y=280)
entry_tamanho_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_tamanho, '%P'), font="Verdana 9 bold", bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=45)
entry_tamanho_cadastro_ferramenta.place(x=300, y=280)

# Campo da Unidade de medida da ferramenta
label_medida_cadastro_ferramenta = Label(text='UNIDADE DE MEDIDA', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_medida_cadastro_ferramenta.place(x=140, y=320)
entry_medida_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_medida, '%P'), font="Verdana 9 bold", bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=45)
entry_medida_cadastro_ferramenta.place(x=300, y=320)

# Campo do Tipo da ferramenta
label_tipo_cadastro_ferramenta = Label(text='TIPO', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_tipo_cadastro_ferramenta.place(x=140, y=360)
entry_tipo_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_tipo, '%P'), font="Verdana 9 bold", bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=45)
entry_tipo_cadastro_ferramenta.place(x=300, y=360)

# Campo do Material da ferramenta
label_material_cadastro_ferramenta = Label(text='MATERIAL', bg=corCinza, fg=corLetra, font="Verdana 12 bold")
label_material_cadastro_ferramenta.place(x=140, y=400)
entry_material_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_material, '%P'), font="Verdana 9 bold", bg=corBranca, highlightbackground=corBorda, fg=corLetra, justify="left", width=45)
entry_material_cadastro_ferramenta.place(x=300, y=400)

# Campo do Tempo máximo de reserva da ferramenta
'''
lista_tempo_ferramenta = [1, 2, 4, 6, 8, 12, 24, 48, 72]
label_tempo_ferramenta = Label(text='TEMPO MÁXIMO DA RESERVA (HORAS)')
label_tempo_ferramenta.place(
combobox_tempo_ferramenta = Combobox(values=lista_tempo_ferramenta)
combobox_tempo_ferramenta.place(
'''

# Botão de cancelar
botao_cancelar_ferramenta = Button(text='CANCELAR', font="Verdana 9 bold", highlightbackground=corBorda, fg=corLetra,  height=2, width=15, command=botao_cancelar)
botao_cancelar_ferramenta.place(x=300, y=440)

# Botão de confirmação
botao_cadastrar_ferramenta = Button(text='CADASTRAR', font="Verdana 9 bold", highlightbackground=corVerde, fg=corLetra,  height=2, width=15, command=botao_cadastrar)
botao_cadastrar_ferramenta.place(x=485, y=440)

# Impressão da tela
janelaCadastroFerramenta.mainloop()
