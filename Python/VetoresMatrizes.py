#Definindo um vetor
from numpy import array
notas_real = array([2, 5, 10, 20, 50, 100, 200], dtype=int)
'''
#Acessando os dados do vetor pelo índice
print(notas_real[1])
print(notas_real[5])
#Alterando um elemento do vetor com input
def alterar():
    print(f'O vetor antes da alteração: {notas_real}')
    indice = eval(input('Digite o índice desejado:'))
    elemento = eval(input('Digite o novo valor:'))
    notas_real[indice] = elemento
    print(f'O vetor após a alteração: {notas_real}')
alterar()
#Iterando o vetor
for elemento in notas_real:
    print(elemento, end=' - ')
'''
'''
#Definindo uma matriz de duas dimensões
cadeiras = array([ ['português', 'matemática', 'inglês'], ['história', 'política', 'finanças'] ], dtype=str)
#Acessando os dados da matriz
print(cadeiras[0][0])
#Alterando um elemento da matriz
cadeiras[0][0] = 'italiano'
print(cadeiras[0][0])
#Iterando a matriz
#listas da matriz
for vetor in cadeiras:
    print(vetor)
    #elementos das listas
    for elemento in vetor:
        print(elemento)
        #letras dos elementos
        for i in elemento:
            print(i)
'''
