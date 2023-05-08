'''
Implementar um algoritmo para imprimir e somar todos os números menores ou iguais a um determinado
número primo.

1• objetivo: Utilizar comandos iterativos e condicionais para desenvolver o algoritmo
2• objetivo: Fornecer um número (N) para o algortimo imprimir e somar todos os números primos menores
ou iguais a N
'''

num = 7
soma = 0

for dividendo in range(2, num + 1):
    contador = 0
    for divisor in range(1, dividendo + 1):
        if dividendo % divisor == 0:
            contador += 1
    if contador == 2:
        print(f'O número {dividendo} é primo.')
        soma = soma + dividendo

print(f'A soma de todos os números primos menores iguais a 7 é: {soma}')









