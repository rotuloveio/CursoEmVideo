# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
num = list()

for i in range(0, 5):
    num.append(int(input(f'Digite um valor para posição {i}: ')))

print(f'Você digitou os valores {num}')

maxi = list()
mini = list()

for i, n in enumerate(num):
    if n == max(num):
        maxi.append(i)
    if n == min(num):
        mini.append(i)

print(f'O maior valor é {max(num)} na(s) posição(ões) ', end='')
for i in maxi:
    print(f'{i} ', end='')
print(f'\nO menor é {min(num)} na(s) posição(ões) ', end='')
for i in mini:
    print(f'{i} ', end='')
