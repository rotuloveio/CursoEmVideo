# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# - quantas pessoas cadastradas.
# - a média de idade.
# - uma lista com mulheres.
# - uma lista com idade acima da média.
pessoas = []
mulheres = []
maiores = []
temp = {}

idades = total = 0

while True:
    temp['Nome'] = input('Nome: ')
    temp['Sexo'] = input('Sexo [M/F]: ')
    temp['Idade'] = int(input('Idade: '))

    pessoas.append(temp.copy())
    if temp['Sexo'] == 'F':
        mulheres.append(temp['Nome'])

    total += 1

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').upper()[0]
    if resp == 'N':
        break

for pessoa in pessoas:
    idades += pessoa['Idade']

media = idades / total

for pessoa in pessoas:
    if pessoa['Idade'] > media:
        maiores.append(pessoa['Nome'])

print(f'{total} pessoa(s) cadastrada(s).')
print(f'A média de idade é de {media} anos.')
print(f'As mulheres são: {mulheres}')
print(f'As pessoas com idade acima da média são: {maiores}')
