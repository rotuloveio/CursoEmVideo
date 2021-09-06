# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# - qual é o total gasto na compra.
# - quantos produtos custam mais de R$1000.
# - qual é o nome do produto mais barato.
mil = total = barato = resp = 0
pbarato = 1000000000000000000000000

while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    total += preco
    if preco > 1000:
        mil += 1
    if preco < pbarato:
        pbarato = preco
        barato = nome
    resp = 0
    while resp != 'S' and resp != 'N':
        resp = input('Você quer continuar [S/N]? ').upper()
    if resp == 'N':
        break

print(f'Total: R${total:.2f}')
print(f'{mil} produto(s) custam mais de R$1000.00.')
print(f'O produto mais barato é {barato} que custa R${pbarato}.')
