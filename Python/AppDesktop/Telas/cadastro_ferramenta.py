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


# Criando a janela
janelaCadastroFerramenta = Tk()

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

# Título da janela
janelaCadastroFerramenta.title('Cadastro de Ferramentas')

# Tamanho da janela
janelaCadastroFerramenta.minsize(width=300, height=300)
janelaCadastroFerramenta.resizable(width=FALSE, height=FALSE)

# Campo da Descrição da janela
label_descricao_cadastro_ferramenta = Label(text='Descrição:')
label_descricao_cadastro_ferramenta.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
entry_descricao_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_descricao, '%P'))
entry_descricao_cadastro_ferramenta.grid(row=1, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)

# Campo do Part Number da ferramenta
label_number_cadastro_ferramenta = Label(text='Part Number:')
label_number_cadastro_ferramenta.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
entry_number_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_number, '%P'))
entry_number_cadastro_ferramenta.grid(row=2, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)

# Campo do Fabricante da ferramenta
label_fabricante_cadastro_ferramenta = Label(text='Fabricante:')
label_fabricante_cadastro_ferramenta.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
entry_fabricante_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_fabricante, '%P'))
entry_fabricante_cadastro_ferramenta.grid(row=3, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)

# Campo da Voltagem da ferramenta
label_voltagem_cadastro_ferramenta = Label(text='Voltagem:')
label_voltagem_cadastro_ferramenta.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
entry_voltagem_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_voltagem, '%P'))
entry_voltagem_cadastro_ferramenta.grid(row=4, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)

# Campo do Tamanho da ferramenta
label_tamanho_cadastro_ferramenta = Label(text='Tamanho:')
label_tamanho_cadastro_ferramenta.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
entry_tamanho_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_tamanho, '%P'))
entry_tamanho_cadastro_ferramenta.grid(row=5, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)

# Campo da Unidade de medida da ferramenta
label_medida_cadastro_ferramenta = Label(text='Unidade de Medida:')
label_medida_cadastro_ferramenta.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
entry_medida_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_medida, '%P'))
entry_medida_cadastro_ferramenta.grid(row=6, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)

# Campo do Tipo da ferramenta
label_tipo_cadastro_ferramenta = Label(text='Tipo:')
label_tipo_cadastro_ferramenta.grid(row=7, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
entry_tipo_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_tipo, '%P'))
entry_tipo_cadastro_ferramenta.grid(row=7, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)

# Campo do Material da ferramenta
label_material_cadastro_ferramenta = Label(text='Material:')
label_material_cadastro_ferramenta.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
entry_material_cadastro_ferramenta = Entry(janelaCadastroFerramenta, validate='key', validatecommand=(vcmd_material, '%P'))
entry_material_cadastro_ferramenta.grid(row=8, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)

# Campo do Tempo máximo de reserva da ferramenta
'''
lista_tempo_ferramenta = [1, 2, 4, 6, 8, 12, 24, 48, 72]
label_tempo_ferramenta = Label(text='Tempo máximo de reserva (horas):')
label_tempo_ferramenta.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
combobox_tempo_ferramenta = Combobox(values=lista_tempo_ferramenta)
combobox_tempo_ferramenta.grid(row=8, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)
'''

# Botão de cancelar
botao_cancelar_ferramenta = Button(text='Cancelar', command=botao_cancelar)
botao_cancelar_ferramenta.grid(row=9, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

# Botão de confirmação
botao_cadastrar_ferramenta = Button(text='Cadastrar', command=botao_cadastrar)
botao_cadastrar_ferramenta.grid(row=9, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)

# Impressão da tela
janelaCadastroFerramenta.mainloop()
