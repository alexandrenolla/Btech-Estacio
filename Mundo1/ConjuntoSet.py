# Os Conjuntos podem ser utilizados para remover itens duplicados de outras sequências ou testes de pertinência e computar operações matemáticas, como união e interseção, entre outras.
# 1. Não homogêneo. 2. Dinâmico 3. Não linear

# Definindo um conjunto. Para inicializarmos um objeto do tipo Set podemos proceder de duas formas:

# Utilizar chaves com elementos separados por vírgulas
conjunto = {1,2,3}

# Utilizar o construtor set(), que aceita como parâmetro outras coleções.
conjunto = set()
conjunto = set((1,2,3))
conjunto2 = set([1,2,3])
print(conjunto, conjunto2)

# Assim como nas Listas, os elementos de um conjunto podem ser de diferentes tipos, desde que o próprio elemento e seus filhos sejam imutáveis, como no exemplo a seguir, em que temos como elementos um número inteiro, uma string e uma tupla:

conjunto3 = {1, 'Hello', (3,4)}
print(conjunto3)
# ^ Apesar dos elementos de um conjunto serem imutáveis, os Conjuntos são coleções mutáveis, ou seja, eles podem ser alterados durante a execução do programa.

# Acessando os dados de um conjunto:
# Como os conjuntos não são lineares, eles não armazenam seus elemetos em índices, portanto precisamos iterar com o método pop.
# Iterando:
print('-------')

conjunto4 = {'a', 1, 2022, (28,12), 'a'} # <- itens duplicados são automaticamente removidos.
for elemento in conjunto4:
    print(elemento) # <- como os conjuntos não são lineares, eles retornam os elementos de forma aleatória.

# Alterando o conjunto
# Inserindo um novo elemento, passado como parâmetro.
conjunto5 = set()
conjunto5.add(1)
conjunto5.add('GOLD')
conjunto5.add('SILVER')
print(conjunto5)

# Extaindo elementos de forma aleatória com o pop.
print('-----')
conjunto5.pop()
print(conjunto5)
print('-----')

# Removendo um elemento,passado como parâmetro.
conjunto5.discard('SILVER')
print(conjunto5)

# Removendo todos os elementos.
conjunto5.clear()
print(conjunto5)

# As funções internas do Python que se aplicam às Listas também se aplicam aos Conjuntos: len, min, max e sum. Os operadores de pertinência (in e not in) e equivalência (==) também podem ser aplicados aos objetos do tipo Set.

# Os objetos do tipo Set disponibilizam alguns métodos relacionados a operações matemáticas. No exemplo a seguir, mostraremos a utilização de alguns deles: union (união), intersection (intercessão) e difference (diferença). Todos esses métodos retornam um novo conjunto.
print('---------')
conjunto_a = {1,2,3}
conjunto_b = {4,5,6}
conjunto_b = {3,4,5}

uniao = conjunto_a.union(conjunto_b)
print(uniao)

intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)

diferenca = conjunto_a.difference(conjunto_b)
print(diferenca)





