# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# - de 1 até 10, de 1 em 1.
# - de 10 até 0, de 2 em 2.
# - uma contagem personalizada.
from time import sleep


def contador(inicio, fim, pulo):
    print('-=' * 20)
    passo = pulo
    if (inicio > fim and pulo > 0) or (inicio < fim and pulo < 0):
        passo = -pulo
    if passo > 0:
        limite = fim + 1
    elif passo == 0:
        if inicio > fim:
            limite = fim - 1
            passo = -1
        else:
            limite = fim + 1
            passo = 1
    else:
        limite = fim - 1

    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')

    for cont in range(inicio, limite, passo):
        print(cont, end=' ')
        sleep(.5)
    print('FIM!')


# PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, -2)
print('-=' * 20)
print('Sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim:    ')), int(input('Passo:  ')))
