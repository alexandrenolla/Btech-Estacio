'''
Implementar um algoritmo para obter o conjunto das partes de um conjunto
1• objetivo: Utilizar estruturas de dados como listas, comandos condicionais e iterativos
2• objetivo: Entrar com uma lista que representa o conjunto e o programa deve produzir o seu
respectivo conjunto das partes.

Resultados esperados:
- Entrada dos dados
- Realização dos cálculos intermediários
- Apresentação da saída: conjunto das partes de um conjunto de entrada
'''
# Importação biblioteca
from itertools import combinations

# Entrada de dados
lista = input('Digite os elementos desejados aqui:').split(',')

# Cálculos intermediários
resultado = []
for i in range(0, len(lista) + 1):
    for combination in combinations(lista, i):
        conversor = list(combination)
        resultado.append(conversor)

# Imprimindo o resultado
print(resultado)

