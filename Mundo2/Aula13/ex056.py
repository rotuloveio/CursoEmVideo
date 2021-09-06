# Desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.
velho = total = mulheres = 0
nomevelho = ''


for i in range(0, 4):
    print(f'---- {i+1}ª PESSOA ----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    if sexo == 'M' and idade > velho:
        nomevelho = nome
        velho = idade
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    total += idade

media = total / 4

print(f'A média de idade do grupo é de {media} anos.')
if velho:
    print(f'O homem mais velho tem {velho} anos e se chama {nomevelho}.')
if mulheres:
    print(f'{mulheres} mulher(es) com menos de 20 anos.')
