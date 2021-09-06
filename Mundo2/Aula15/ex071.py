# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa cai informar quantas
# cédulas de cada valor serão entregues.
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
saque = int(input('Quanto você quer sacar? R$'))

cinq = saque // 50
saque %= 50

vint = saque // 20
saque %= 20

dez = saque // 10

um = saque % 10

if cinq:
    print(f'{cinq} cédula(s) de R$50')
if vint:
    print(f'{vint} cédula(s) de R$20')
if dez:
    print(f'{dez} cédula(s) de R$10')
if um:
    print(f'{um} cédula(s) de R$1')
