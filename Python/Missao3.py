# Implementar um algoritmo para obter o conjunto das partes de um conjunto.
from itertools import combinations

lista = input('Digite os elementos desejados aqui:').split(',')
resultado = []
for i in range(0, len(lista) + 1):
    for combination in combinations(lista, i):
        conversor = list(combination)
        resultado.append(conversor)
print(resultado)

