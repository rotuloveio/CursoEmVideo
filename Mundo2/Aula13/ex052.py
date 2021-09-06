# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
from math import sqrt, ceil

n = int(input('Digite um número: '))

p = 1

for i in range(2, ceil(sqrt(n))):
    if n % i == 0:
        p = 0
        break

if p:
    print(f'{n} é primo.')
else:
    print(f'{n} não é primo.')
