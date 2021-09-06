# Crie um programa que leia dois valores e mostre o seguinte menu:
# 1 - somar
# 2 - multiplicar
# 3 - maior
# 4 - novos números
# 5 - sair
n1 = n2 = menu = 4
while menu != 5:
    if menu == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    menu = int(input('O que fazer: \n1 - somar\n2 - multiplicar\n3 - maior\n4 - novos números\n5 - sair\n'))
    if menu == 1:
        print(f'A soma de {n1} com {n2} é {n1+n2}.')
    elif menu == 2:
        print(f'O produto entre {n1} e {n2} é {n1 * n2}.')
    elif menu == 3:
        if n1 > n2:
            print(f'O maior é {n1}.')
        else:
            print(f'O maior é {n2}.')
