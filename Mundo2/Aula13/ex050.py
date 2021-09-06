# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
s = 0
for i in range(0, 6):
    n = int(input(f'Digite o {i+1}º número: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos pares é {s}.')
