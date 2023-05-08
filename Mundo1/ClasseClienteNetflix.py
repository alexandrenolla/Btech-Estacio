# vamos criar uma classe para Clientes da Netflix
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['Basic', 'Premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano Inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver Filme {filme}')
        elif self.plano == 'Premium':
            print(f'Ver Filme {filme}')
        elif self.plano == 'Basic' and plano_filme == 'Premium':
            print('Faça upgrade de plano para assistir esse filme.')
        else:
            print('Plano Inválido')


# Instância cliente criado com plano basic
cliente = Cliente("Alexandre", "alexandre.nolla@gmail.com", "Basic")
print(cliente.plano)
# Instância cliente impedido de acessar filme do plano premium
cliente.ver_filme('Harry Potter', 'Premium')

# Instância cliente executando botão de upgrade
cliente.mudar_plano('Premium')
print(cliente.plano)
# Instância cliente atualizado para plano premium
cliente.ver_filme('Harry Potter', 'Premium')
