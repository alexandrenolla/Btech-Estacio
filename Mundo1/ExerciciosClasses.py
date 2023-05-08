# Implementar um programa Python para criar uma classe Veiculo com atributos de
# instância "velocidade máxima" e "quilômetros percorridos por litro."


class Veiculo:
    def __init__(self, nome, velocidade_maxima, quilometros_litro):
        self.nome = nome
        self.velocidade_maxima = velocidade_maxima
        self.quilometros_litro = quilometros_litro

    def valores(self):
        print(f'nome = {self.nome}')
        print(f'velocidade máxima = {self.velocidade_maxima}')
        print(f'quilometros por litro = {self.quilometros_litro}')


maria_gasolina = Veiculo("porsche", 240, 10)
print(maria_gasolina.valores())

#  Crie uma classe filha Ônibus que herdará todas as variáveis e métodos da classe
#  Veículo e ainda forneça a quantidade de assentos.


class Onibus(Veiculo):
    def __init__(self, nome, velocidade_maxima, quilometros_litro, lotacao):
        super().__init__(nome, velocidade_maxima, quilometros_litro)
        self.lotacao = lotacao

    def capacidade(self):
        return self.lotacao


volvo = Onibus("volvo", 120, 60, 30)
print(f'{volvo.valores()} Lotação:  {volvo.capacidade()}')
