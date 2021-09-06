# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
nome = input('Qual sua cidade? ')
dividido = nome.upper().split()

print('SANTO' in dividido[0])
