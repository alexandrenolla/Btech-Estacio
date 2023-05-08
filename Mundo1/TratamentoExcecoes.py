# Implementar solução que faça o tratamento de exceção para verificar se a entrada é um número.
'''
try:
    x = int(input('Digite um número:'))
except ValueError:
    print('Entre com um número válido.')
'''

#Implementar solução que faça o tratamento de exceção para verificar se uma entrada é numérica e que, além disso, insista que o usuário digite um número válido.
'''
while True:
    try:
        x = int(input('Digite um número:'))
        break
    except ValueError:
        print('Entre com um número válido.')
'''

#Implementar solução que faça o tratamento de exceção de divisão por zero.

#estratégia 01
'''
def dividir(x, y):
    try:
        resultado = x / y
        print('A resposta é:', resultado)
    except ZeroDivisionError:
        print('Divisão por zero.')
dividir(2, 0)
'''



