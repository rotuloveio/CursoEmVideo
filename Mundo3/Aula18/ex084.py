# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# - quantas pessoas foram cadastradas.
# - uma listagem com as pessoas mais pesadas.
# - uma listagem com as pessoas mais leves.
pessoas = list()
total = 0
while True:
    temp = list()
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    pessoas.append(temp[:])
    del temp
    total += 1

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').upper()[0]

    if resp == 'N':
        break

maior = 0
menor = 1000

maiores = list()
menores = list()

for pessoa in pessoas:
    if pessoa[1] > maior:
        maior = pessoa[1]
    if pessoa[1] < menor:
        menor = pessoa[1]

for pessoa in pessoas:
    if pessoa[1] == maior:
        maiores.append(pessoa[0])
    if pessoa[1] == menor:
        menores.append(pessoa[0])

print(f'{total} pessoa(s) cadastrada(s).')
print(f'O maior peso foi de {maior}kg. Peso de {maiores}')
print(f'O menor peso foi de {menor}kg. Peso de {menores}')
