# Faça um programa que leia um número qualquer e mostre o seu fatorial.
m = n = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {m}! =', end='')
f = 1
while n > 1:
    print(f' {n} x', end='')
    f *= n
    n -= 1

print(f' 1 = {f}')
