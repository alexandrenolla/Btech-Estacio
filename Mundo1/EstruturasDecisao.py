# Implementar uma solução em Python que receba dois número e identifique qual o maior deles
'''
n1 = eval(input('Digite o primeiro número:'))
n2 = eval(input('Digite o segundo número:'))
if n1 < n2:
    print(f'O menor número é {n1}')
else:
    print(f'O menor número é {n2}')
'''

#Implementar solução que verifique se um número é par ou ímpar
'''
n1 = eval(input('Digite o número desejado:'))
if n1 % 2 == 0:
    print(f'O número {n1} é par')
else:
    print(f'O número {n1} é ímpar')
'''

#Implementar Solução que resolva:
# - Se a nota for maior ou igual a 7, o estudante foi aprovado.
#- Se a nota for menor que 7 e maior ou igual a 5, o estudante está em recuperação.
#- Se a nota for menor que 5, o estudante está reprovado.
'''
nota = eval(input('Digite a nota do estudante:'))
if nota >= 7:
    print('O estudante está aprovado!')
elif nota >= 5:
    print('O estudante está em recuperação.')
else:
    print('O estudante foi reprovado.')
'''

# Implementar solução que resolva:
#- Calcular o valor de uma compra, sendo que o preço unitário é 10.
#- Se for feita uma compra de até 10 unidades, não há descontos.
#- Para compras entre 11 e 20 unidades é dado um desconto de 10%.
#- Acima de 20 unidades, é dado um desconto de 20%.
"""
unidade = 10
quantidade = eval(input('Quantas unidades você comprou?'))
preco = quantidade * unidade
desconto = 0
if quantidade <= 10:
    desconto = 0
elif quantidade <= 20:
    desconto = preco * 0.10
elif quantidade > 20:
    desconto = preco * 0.20
total = preco - desconto
print(f'Você comprou {quantidade} unidades e seu desconto foi de {desconto}. Portanto você pagará {total} reais.')
"""

#Implementar solução que some todos os números pares de uma lista.
# estratégia 1
'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 19, 20]
n = len(lista)
soma = 0
for i in range(n):
    if lista[i] % 2 == 0:
        soma += lista[i]
print(soma)
'''

# estatrégia 2 e melhor
'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 19, 20]
soma = 0
for num in lista:
    if num % 2 == 0:
        soma = soma + num
print(soma)
'''
