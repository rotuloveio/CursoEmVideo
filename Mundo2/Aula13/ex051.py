# Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética.
# No final, mostre os 10 primeiros termos dessa progressão.
n1 = int(input('Digite o primeiro termo da PA: '))
ra = int(input('Digite a razão da PA: '))

for i in range(0, 10):
    print(n1+i*ra)
