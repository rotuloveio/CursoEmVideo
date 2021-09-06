# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - o primeiro valor é maior.
# - o segundo valor é maior.
# - os valores são iguais.
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print(f'O primeiro é maior.')
elif n1 < n2:
    print(f'O segundo é maior.')
else:
    print(f'Os números são iguais.')
