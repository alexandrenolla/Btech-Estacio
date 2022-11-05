# Ao contrário das listas, pilhas e filas, as tuplas são estáticas, não podendo variar de tamanho durante a execução do programa.
# Definindo uma tupla vazia:
tupla = ()

# Definindo uma tupla com elementos, com ou sem parentêses
tupla = ('a','b','c')
tupla = 'a','b','c'

# Para iniciar uma tupla de apenas um item, deve-se colocar uma vírgula após o item.
tupla = 'a',

# O construtor tuple aceita como parâmetro outras coleções, porém apenas 1 argumento.
tupla = tuple([1,2,3,'a'])
print(tupla)
tupla = tuple((1,2,3,'a'))
print(tupla)

# Assim como nas listas, os elementos de uma tupla podem ser de diferentes tipos, incluindo outra tupla, porém elas não podem ser alteradas durante a execução:
tupla = (1, 'Hello', [1,2], (3,4))
print(tupla)

# Acessando os dados da tupla:
item = tupla[2]
print(item)

# Assim como nas listas, podemos utilizar o método index para encontrar o índice de um elemento.
item = tupla.index('Hello')
print(item)

# Como as tuplas são imutáveis, se tentarmos alterar um elemento utilizando o índice, o sistema retornará um erro (TypeError).

'''tupla[2] = 'd' '''

# Iterando a Tupla
print('-----------')
for elemento in tupla:
    print(elemento)

# As funções internas do Python aplicadas às listas também se aplicam às Tuplas: len, min, max e sum, assim como os operadores de pertinência (in e not in), equivalência (==), concatenação (+) e multiplicação (*), também podem ser aplicados aos objetos do tipo tuple. Isso se dá porque todas essas funções e operadores retornam um novo valor e não alteram a tupla.

# Nomeando as Tuplas:

agenda = {('João', 'Silva'): '2222'}
print(agenda[('João', 'Silva')])

import collections

pessoa = collections.namedtuple('Pessoa', 'nome idade')

homem = pessoa(nome='João', idade='25')
print(homem.nome)