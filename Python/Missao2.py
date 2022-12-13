'''
Implementar um algoritmo de conversão de um número da base decimal para base binária

1• objetivo: Utilizar recursos lógicos da linguagem Python, com comandos iterativos
2• objetivo: Entrar com qualquer número inteiro positivo na base decimal e o programa
deve produzir o número correspondente na base binária
'''

numero = int(input('Digite qualquer número inteiro positivo: '))
print(f'Número na base decimal: {numero}')

resto = []
while numero > 0:
    quociente = numero % 2
    resto.append(quociente)
    numero = numero // 2
resto.reverse()
binario = ""

for algarismo in resto:
    binario = binario + str(algarismo)

print(f'Número na base binária: {binario}')

''' Estratégia 2 ->
def decimal_para_binario(decimal):
    binario = ''	
    while decimal > 0:
        binario+= str(decimal%2)
        decimal//= 2
    return binario[::-1]
'''