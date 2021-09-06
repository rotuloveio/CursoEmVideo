# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nomes separadamente.
nome = input('Qual seu nome? ').split()


print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[len(nome)-1]}')
