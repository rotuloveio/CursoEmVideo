# Faça um programa que leia uma frase pelo teclado e mostre:
# - quantas vezes aparece a letra "A".
# - em que posição ela aparece a primeira vez.
# - em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').upper()

print(frase.count('A'))
print(frase.find('A'))
print(frase.rfind('A'))
