import tkinter
from tkinter import Button, Entry, Label, messagebox, PhotoImage
import Imc

def acao():
    print('Botão clicado!')
# Método .get() serve para capturar o texto inserido nas caixas de entrada. Nesse caso, estamos passando o input como argumentos para a função calcula_imc.
    
# Logo, o resultado retornado é armazenado na variável indice, que é utilizada como argumento da função classifica_imc.
    indice = imc.calcula_imc(peso=peso.get(), altura=altura.get())
    media = imc.classifica_imc(indice)
    msg = messagebox.showinfo("Classificação IMC:", media)


# Criando a janela da interface
principal = tkinter.Tk()
# Código da interface aqui.

# Logo
# Classe para inserir imagens, passando o path do arquivo como argumento.
imagem = PhotoImage(file="estacio.png")

# Etiqueta da imagem. 1. Qual janela? 2. Qual elemento?
logo = Label(master=principal, image=imagem)

# Posicionando a imagem na tabela.
logo.grid(row=0, column=0, rowspan=2)

# Etiqueta do campo Altura: 1. Qual janela? 2. Qual texto?
etiqueta_altura = Label(principal, text='Altura:')
#Posicionamento
etiqueta_altura.grid(row=0, column=1)

# Caixa de entrada da Altura e posicionamento
altura = Entry(principal)
altura.grid(row=0, column=2)

# Etiqueta do campo Peso: 1. Qual janela? 2. Qual texto?
etiqueta_peso = Label(principal, text='Peso:')
# Posicionamento
etiqueta_peso.grid(row=1, column=1)


# Caixa de entrada do Peso e posicionamento
peso = Entry(principal)
peso.grid(row=1, column=2)

# Botão para Calcular: 1. Qual janela? 2. Qual texto? 3. Qual função?
botao = Button(principal, text='Calcular:', command=acao)
# Posicionamento
botao.grid(row=2, column=2)

# Execução da janela
principal.mainloop()

