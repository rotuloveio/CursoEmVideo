# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - o nome com todas as letras maiúsculas e minúsculas.
# - quantas letras ao total (sem considerar espaços).
# - quantos letras tem o primeiro nome.
nome = input('Qual seu nome? ')
print(nome.upper())
print(nome.lower())
dividido = nome.split()
total = 0
for palavra in dividido:
    total += len(palavra)
print(total)
print(len(dividido[0]))
