import tkinter as tk

def cadastrar():
    # Comando para gerar nova janela
    janelaCadastro = tk.Toplevel()
    janelaCadastro.title('Cadastrar Ferramenta')
    label_janelaCadastro = tk.Label(janelaCadastro, text='Ferramenta:')
    label_janelaCadastro.grid(row=0, column=0)
    botaoVoltar = tk.Button(janelaCadastro, text='Voltar', command=janelaCadastro.destroy)
    botaoVoltar.grid(row=0, column=0)



janelaPrincipal = tk.Tk()
janelaPrincipal.title('Bem vindo à Ferramentaria')
botao = tk.Button(janelaPrincipal, text='Cadastrar', command=cadastrar)
botao.grid(row=3, column=3)

janelaPrincipal.mainloop()