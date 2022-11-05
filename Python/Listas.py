# Definindo uma lista vazia
listaVazia = []
# Definindo uma lista com elementos do mesmo tipo
listaSimples = ['a', 'b', 'c']
# Definindo uma lista com diferentes tipos de parâmetros, inclusive outra lista
listaCompleta = list([1, 2, 3, 'a', 'b', 'c', [5, 6]])
# Acessando elementos da lista
print(listaCompleta[6])
# Descobrindo o índice pelo método index
indiceC = listaCompleta.index('c')
print(indiceC)
# Alterando os dados pelo índice
print(listaCompleta)
listaCompleta[5] = 'FUCKING DOLLARS'
print(listaCompleta)
# Iterando a lista
for elemento in listaCompleta:
    print(elemento)
print('--------------------')
# Acessando os elementos através de seus índices
for i in range(0, len(listaCompleta)):
    print(listaCompleta[i])
# Alterando a lista. Inserindo elemento passado como parâmetro no final da lista
listaCompleta.append('GOLD')
print(listaCompleta)
# Alterando a lista. Inserindo elemento na posição indicada no parâmetro.
listaCompleta.insert(7,'DIAMOND')
print(listaCompleta)
print('------------')
# Concatenando duas listas, passando a segunda lista como parâmetro
listaCompleta.extend(listaSimples)
print(listaCompleta)
# Removendo o elemento da lista passado como parâmetro
listaCompleta.remove([5, 6])
print(listaCompleta)
# Removendo todos os elementos de uma lista
listaSimples.clear()
print(listaSimples)
# Invertendo os elementos da lista
listaNumerica = [1, 14, 33, 20, 99, 7]
listaNumerica.reverse()
print(listaNumerica)
# Ordenando os elementos da lista (incompatível com mais de um tipo na lista).
listaNumerica.sort()
print(listaNumerica)
# Retornando o tamanho, o elemento de valor mínimo, o elemento de valor máximo e a soma dos elementos da lista, respectivamente.
print(len(listaNumerica))
print(min(listaNumerica))
print(max(listaNumerica))
print(sum(listaNumerica))
# Combinando funções
media = sum(listaNumerica) / len(listaNumerica)
print(media)
print('--------------------')
# Operadores nas listas: 1. Pertinência (in, not in). 2. equivalência (==). 3. concatenação(+). 4. multiplicação (*).
#Todos retornam algum objeto, como um Booleano ou como uma nova lista, podendo ser utilizados em condicionantes if.

lista1 = [1,2,3]
lista2 = [1,2,3]
lista3 = [4,5,6]
print(lista1 == lista2)
print(lista2 == lista3)

if 3 in lista1:
    print('Achei o 3!')

nova_lista = lista1 + lista3
print(nova_lista)

lista_repetida = lista1 * 4
print(lista_repetida)
print('---------')
#Lists Comprehensions
Lista = [0,1,2,3,4,5,6]
Nova_lista = [elemento*2 for elemento in Lista if elemento % 2 == 0]
print(Nova_lista)


