class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender

    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender
# Definindo Objetos para Classe Pessoa
pessoa1 = Pessoa('Maria Carolina', 'Rua das Moreas')
pessoa2 = Pessoa('Alexandre Henrique', 'Rua das Moreas')
# Imprimindo os atributos dos objetos
print(f'Nome da cidadã: {pessoa1.get_nome()}. Endereço dela: {pessoa1.get_ender()}')
print(f'Nome do cidadão: {pessoa2.get_nome()} Endereço dele: {pessoa2.get_ender()}')

