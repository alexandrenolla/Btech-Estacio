import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar = {cotacao_dolar}
    Euro = {cotacao_euro}
    Btc = {cotacao_btc}'''

    exibir_cotacoes['text'] = texto


janelaPrincipal = Tk()
janelaPrincipal.title("Verificador de Cotações")
# janelaPrincipal.geometry('400x400')
descricaojanelaPrincipal = Label(janelaPrincipal, text='Clique para exibir as cotações das moedas')
descricaojanelaPrincipal.grid(column=0, row=0, padx=10, pady=10)
botao = Button(janelaPrincipal, text='Ver', command=pegar_cotacoes)
botao.grid(column=0, row=1)
exibir_cotacoes = Label(janelaPrincipal, text='')
exibir_cotacoes.grid(column=0,  row=2)


janelaPrincipal.mainloop()
