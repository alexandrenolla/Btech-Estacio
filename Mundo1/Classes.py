# Classe com 2 atributos: nome e idade.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
# Método para atribuir o nome a um objeto
    def setNome(self, nome):
        self.nome = nome
# Método para atribuir a idade a um objeto
    def setIdade(self, idade):
        self.idade = idade
# Método para informar o nome de um objeto
    def getNome(self):
        return self.nome

# Método para informar a idade de um objeto
    def getIdade(self):
        return self.idade