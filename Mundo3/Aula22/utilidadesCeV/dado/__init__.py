def leiadinheiro(msg):
    while True:
        entrada = str(input(msg)).strip().replace(',', '.')
        if not entrada.isalpha() and entrada != '':
            return float(entrada)
        print(f'\033[31mERRO: "{entrada}" não é um preço válido.\033[m')


def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[31mDigite um número inteiro válido.\033[m')
    return valor
