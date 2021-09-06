# Desenvolva um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final do programa, mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres têm menos de 20 anos.
cont = sexo = mulher = homem = maior = 0

while True:
    print('CADASTRE UMA PESSOA:')
    idade = int(input('Digite a idade: '))
    sexo = 0
    while sexo != 'M' and sexo != 'F':
        sexo = input('Digite o sexo [M/F]: ').upper()
    cont = 0
    while cont != 'S' and cont != 'N':
        cont = input('Você quer continuar [S/N]? ').upper()

    if idade >= 18:
        maior += 1

    if sexo == 'M':
        homem += 1

    if sexo == 'F' and idade < 20:
        mulher += 1

    if cont == 'N':
        break

if maior:
    print(f'{maior} pessoa(s) são maiores de 18 anos.')
else:
    print(f'Ninguem é maior de 18 anos.')

if homem:
    print(f'{homem} homem(ns).')
else:
    print(f'Não há homens.')

if mulher:
    print(f'{mulher} mulher(es) menor(es) de 20 anos.')
else:
    print(f'Não há mulheres menores de 20 anos.')
