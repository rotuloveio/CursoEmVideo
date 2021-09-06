# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input('Digite uma frase: ').upper().split()

spaceless = ''.join(frase)

reverso = spaceless[::-1]

if spaceless == reverso:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
