print('Módulo IMC importado com sucesso.')

def calcula_imc(peso, altura):
    print('Parâmetro peso:', peso)
    print('Parâmetro altura:', altura)
    imc = float(peso) / float(altura) ** 2
    return imc

def classifica_imc(indice):
    if indice < 18.5:
        return 'Baixo peso'
    elif indice < 25:
        return 'Peso adequado'
    elif indice < 30:
        return 'Sobrepeso'
    else:
        return 'Obseso'