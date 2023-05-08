#Implementar solução que retorne o menor elemento de uma lista

# definindo função
'''
def encontrar_minimo(lista):
    minimo = lista[0]
    for i in lista:
        if(i < minimo):
            minimo = i
    return minimo
lista = [4, 3, 2, 6, 8, 1, 5, 7, 9, 10]
resultado = encontrar_minimo(lista)
print(resultado)
'''
# chamando função
'''
menor = encontrar_minimo(lista_teste)
print(f'O menor elementa da lista é {menor}')
'''
#Implementar solução que some todos os números pares de uma lista.
# estratégia 01
'''
def ehPar(n):
    r = (n%2==0)
    return r

def somar_par(lst):
    soma = 0
    for num in lst:
        if(ehPar(num)):
            soma = soma + num
    return soma

lista = [10, 2, 5, 7, 6, 3]
soma = somar_par(lista)
print(f'A soma dos elementos pares da lista é: {soma}')
'''
# estratégia 02 (minha)
'''
def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma

lista_teste = [1, 2, 3, 4, 5, 6 ,7, 8]
resultado = soma_pares(lista_teste)
print(resultado)
'''

# Função recursiva para fatorial: estratégia 01
'''
def fatorial(n):
    f = 1
    for i in range(1, n+1):
        f=f*i
    return f


resultado = fatorial(9)
print(resultado)
'''

# Função recursiva para fatorial: estratégia 02
'''
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)


resultado = fatorial(9)
print(resultado)
'''

# Função iterativa para fatorial:
'''
def fatorial(n):
  fatorial = 1
  while (n):
    fatorial *= n
    n -= 1
  return fatorial

resultado = fatorial(5)
print(resultado)
'''

# Função recursiva para Fibonacci. Determina o n-ésimo termo da sequência.
'''
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
# Docstring -> Definição da função abaixo mediante utilitário help com a função passado como parâmetro.
print(help(fibo))
'''

# Função iterativa para Fibonacci. Determina o n-ésimo termo da sequência.
'''
def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n + 1):
               fat = fat*x
        return fat
'''

# Implementar uma solução em Python que determine se um número é ou não primo.
'''
def eh_primo(n):
    if n < 2:
        return False
    i = n// 2
    while i > 1:
        if n%i == 0:
            return False
        i = i - 1
    return True

def imprimir_resultado(numero, resultado):
    mensagem = f'O número {numero} não é primo.'
    if resultado:
        mensagem = f'O número {numero} é primo.'
        return mensagem

numero = 14
resultado = eh_primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)
'''



