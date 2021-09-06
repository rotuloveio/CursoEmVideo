# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

agora = date.today().year

maior = 0
menor = 0
for i in range(0, 7):
    ano = int(input(f'Digite o {i+1}º ano de nasc.: '))
    idade = agora - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoa(s) são maiores e {menor} pessoa(s) são menores.')
