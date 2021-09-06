# Escreva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('\033[1;32m-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Podem formar um triângulo.')
else:
    print('Não podem formar um triângulo.')
