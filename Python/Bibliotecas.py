# Implementar uma solução em Python que calcule as raízes de uma equação de segundo grau.
'''
def entrada_dados():
    coeficiente = quantidade = eval(input('Digite o valor do coeficiente:'))
    return coeficiente

def calc_delta(a, b, c):
    delta = b*b-4*a*c
    return delta

import numpy as np

def calcular_raizes(a, b, c, delta):
    if delta < 0:
        resultado = 'a equação não possui raízes nos números reais.'
    elif delta == 0:
        x =- b/ (2*a)
        resultado = f'a equação possui apenas a raiz: {x}'
    else:
        x1 = (-b-np.sqrt(delta))/(2*a)
        x2 = (-b+np.sqrt(delta))/(2*a)
        resultado = f'a equação possui as raízes: {x1}, {x2}'
    return resultado

# f(x)= axˆ2+bx+c
a = entrada_dados()
b = entrada_dados()
c = entrada_dados()

delta = calc_delta(a, b, c)

resultado = calcular_raizes(a, b, c, delta)
print(resultado)
'''

# Implementar uma solução para visualizar dados de vendas de produtos em um gráfico de barras.
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()
'''

#Implementar solução para gerar 1.000 pontos seguindo a distribuição Normal com média 20 e desvio-padrão 2, sendo exibido em um histograma.
'''
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)
dados = np.random.normal(loc=20, scale=2, size=1000)

plt.hist(dados, color='lightblue', ec='red')
'''
