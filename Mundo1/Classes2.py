from Classes import Pessoa
# Criando um objeto da classe Pessoa que tem Fulano/25 como valores dos atributos nome/idade
pessoa1 = Pessoa('Fulano', 25)
# Método get -> Encapsulamento
print(f'O nome da pessoa1 é {pessoa1.getNome()} e a idade é: {pessoa1.getIdade()}')

# Classe PessoaFisica filha da Classe Pessoa
class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade):
        # Herança: Classe PessoaFisica herda da Classe Pessoa tudo que ela já tem.
        super(). __init__(nome,idade)
        # Atributo novo
        self.CPF = cpf
    # Método para atribuir o atributo novo
    def setCPF(self, cpf):
        self.cpf = cpf
    # Método para retornar o atributo novo
    def getCPF(self, cpf):
        return self.cpf