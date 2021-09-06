# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input("Digite um ano: "))
print('É bissexto.' if ano % 4 == 0 else f'Não é bissexto.')
