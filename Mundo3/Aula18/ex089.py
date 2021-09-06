# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno.
alunos = list()

while True:
    aluno = list()
    notas = list()
    nome = input('Nome: ')
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))

    notas.append(nota1)
    notas.append(nota2)

    aluno.append(nome)
    aluno.append(notas[:])

    alunos.append(aluno[:])

    del aluno
    del notas

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').upper()[0]
    if resp == 'N':
        break

print('Nº NOME {:>15}'.format('MÉDIA'))
for index, aluno in enumerate(alunos):
    media = (aluno[1][0] + aluno[1][1]) / 2
    print(f'{index:<3}{aluno[0]:10}{media:>10.1f}')

while True:
    index = -1
    while index < 0 or index > len(alunos) - 1 and index != 999:
        index = int(input('Mostra notas de qual aluno [999 p/ parar]? '))
    if index == 999:
        break
    print(f'As nodas de {alunos[index][0]} são {alunos[index][1]}.')