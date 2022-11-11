from tkinter import *
from tkinter import messagebox


def Clique():
    print('Você clicou!')
    # Método para criar janela de alerta com o input do evento.
    msg = messagebox.showinfo("Você clicou!", texto.get())


# Criando um objeto da classe Tk. Tk = construtor da janela.
janela = Tk()

# Label = elemento de texto(etiqueta). Parâmetros: 1. Vinculado com quem? 2. Qual texto do elemento??
frase = Label(master = janela, text = 'Minha primeira janela')

# Método para posicionar o elemento centralizado e no topo.
"""frase.pack()"""

# Método para dispor os elementos como em uma tabela.
frase.grid(row=0, columnspan=2)

# Classe para criar caixa de texto de uma linha.
texto = Entry(janela)

# Método para dispor os elementos como em uma tabela.
texto.grid(row = 1, column = 1)

# Label = elemento de texto(etiqueta). Parâmetros: 1. Vinculado com quem? 2. Qual texto do elemento??
etiquetaEntry = Label(master=janela, text='Digite aqui:')

# Método para dispor os elementos como em uma tabela.
etiquetaEntry.grid(row= 1, column =0)

# Button = elemento de botão. Parâmetros: 1. Vinculado com quem? 2. Qual texto do elemento? 3. Parâmetro: Qual argumento(função) do elemento?
botao = Button(master = janela, text = 'Clique aqui', command = Clique)

# Método para posicionar o elemento centralizado e no topo.
"""botao.pack()"""

# Método para dispor os elementos como em uma tabela.
botao.grid(row=2, columnspan=2)

# Método para chamar a exibição da janela.
janela.mainloop()
