# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
num = int(input('Digite um número: '))
base = int(input('Escolha a base (1 - binário, 2 - octal, 3 - hexadecimal) '))

if base == 1:
    print(f'{num} em binário é {bin(num)}')
elif base == 2:
    print(f'{num} em octal é {oct(num)}')
else:
    print(f'{num} em hexadecimal é {hex(num)}')
