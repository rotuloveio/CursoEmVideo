# Faça um programa que tenha uma função chamada área(), que recebe as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.
def area(a, b):
    print(f'A área de um terreno {a} x {b} é de {a*b}m².')


print('Controle de Terrenos')
print('-' * 20)
area(float(input('Largura [m]: ')), float(input('Comprimento [m]: ')))
