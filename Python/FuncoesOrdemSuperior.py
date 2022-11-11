# script selecao.py
"""def selecionador(seq, teste):
    selecionados = []
    for elemento in seq:
        if (teste(elemento)):
            selecionados.append(elemento)
    return selecionados


def verifica_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


# parte principal do programa
def main():
    lista = [0,1,2,3,10]
    numeros_pares = selecionador(lista, verifica_par)
    for num in numeros_pares:
        print(f'{num} -> par')


if __name__ == '__main__':
    main()
print(main)"""


# script potencia.py
def calcula_potencia(expoente):
    def potencia(base):
        return base**expoente
    return potencia


# parte principal do programa
def main():
    base_expoente = input()

# separa base e expoente, convertendo-os para inteiros
    base, expoente = (int(i) for i in base_expoente.split())

# utilizando a função calcula_potencia
    potencia_de = calcula_potencia(expoente)
    res_potencia = potencia_de(base)
    print(f'{base} elevado ao {expoente} = {res_potencia}')


if __name__ == '__main__':
    main()
    print(main)
