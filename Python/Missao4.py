#  Implementar um programa orientado a objetos para visualizar e aplicar regressão
#  linear em séries temporais

import matplotlib.pyplot as plt

alimentacao = {
    1: 50, 2: 30, 3: 150, 4: 100, 5: 30, 6: 80, 7: 50
}
transporte = {
    1: 20, 2: 30, 3: 50, 4: 20, 5: 20, 6: 50, 7: 0
}
vestuario = {
    1: 300, 2: 0, 3: 0, 4: 50, 5: 0, 6: 0, 7: 0
}


class Despesas:
    def __init__(self, alimentacao, transporte, vestuario):
        self.alimentacao = alimentacao
        self.transporte = transporte
        self.vestuario = vestuario

    def setAlimentacao(self, alimentacao):
        self.alimentacao = alimentacao

    def setTransporte(self, transporte):
        self.transporte = transporte

    def setVestuario(self, vestuario):
        self.vestuario = vestuario

    def getAlimentacao(self, alimentacao):
        return alimentacao

    def getTransporte(self, transporte):
        return transporte

    def getVestuario(self, vestuario):
        return vestuario


x = [1, 2, 3, 4, 5, 6, 7] # dias
y = [50, 30, 150, 100, 30, 80, 50] # alimentacao
y2 = [20, 30, 50, 20, 20, 50, 0] # transporte
y3 = [300, 0, 0, 50, 0, 0, 0] # vestuario
plt.plot(x, y, color='green', label='Alimentação', marker='o')
plt.plot(x, y2, color='blue', label='Transporte', marker='o')
plt.plot(x, y3, color='red', label='Vestuario', marker='o')
plt.legend()

plt.title('Gráfico de despesas', color='black', fontsize=16)
plt.xlabel('Dias')
plt.ylabel('Despesa em R$')
plt.show()



