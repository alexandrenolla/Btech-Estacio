import copy

# Operador de atribuição: compartilha só as referências; alterar em uma indiretamente causa alteração na outra.
'''lista1 = [[1,2,3], [4,5,6], [7,8,9]]
lista2 = lista1
lista2[2][2] = 10
print('Lista 1:', lista1)
print('Lista 2:', lista2)'''

# Função copy: Shallow copy -> É criado um objeto novo que compartilha as referências aos elementos originais. Ou seja, os novos elementos criados a partir da cópia poderão ser alterados independentemente, porém os elementos originais copiados continuarão causando alterações na lista original de referência.
'''lista1 = [[1,2,3], [4,5,6], [7,8,9]]
lista2 = copy.copy(lista1)
lista2[2][2] = 10
print('Lista 1:', lista1)
print('Lista 2:', lista2)
lista2.append([10,11,12])
print('Lista 1:', lista1)
print('Lista 2:', lista2)'''

# Função copy: Deep copy -> Permite que façamos alterações completamente independentes, seja no original ou na cópia.
lista1 = [[1,2,3], [4,5,6], [7,8,9]]
lista2 = copy.deepcopy(lista1)
lista2[2][2] = 10
print('Lista 1:', lista1)
print('Lista 2:', lista2)
lista2.append([10,11,12])
print('Lista 1:', lista1)
print('Lista 2:', lista2)