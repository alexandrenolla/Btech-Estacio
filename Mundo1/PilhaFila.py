# Pilha: É um objeto tipo list que só pode ser alterado pelo final.

pilha = []
print('Manipulando pilhas com os métodos adequados:', pilha)
# Adicionando elementos na pilha
pilha.append(1)
pilha.append(2)
pilha.append(3)
print(pilha)
# Removendo elementos da pilha
pilha.pop()
pilha.pop()
pilha.pop()
print(pilha)

# Fila: É um objeto tipo list que só pode ter seus elementos adicionados pelo final e removidos pelo início.
fila = []
print('Manipulando pilhas com os métodos adequados:', fila)
fila.append(1)
fila.append(2)
fila.append(3)
print(fila)
# Retorna e remove o primeiro elemento da fila
fila.pop(0)
print(fila)
fila.pop(0)
print(fila)