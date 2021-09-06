# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
menor = 1000000000000
maior = soma = total = 0
continuar = 'S'
while continuar != 'N':
    num = float(input('Digite um número: '))
    total += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    continuar = input('Continuar? [S/N] ').upper()

print(f'O menor valor é {menor}, o maior é {maior} e a média é {soma / total}')
