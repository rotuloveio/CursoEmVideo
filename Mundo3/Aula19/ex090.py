# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela
aluno = {}
aluno['Nome'] = input('Nome do aluno: ')
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

aluno['Situação'] = 'aprovado' if aluno['Média'] >= 7 else 'reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
