# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 1000

for i in range(0, 5):
    peso = float(input(f'Digite o peso da {i+1}ª pessoa: '))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso

print(f'O maior peso é {maior}kg e o menor é {menor}kg.')
