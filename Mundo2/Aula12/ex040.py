# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# - média abaixo de 5.0: REPROVADO
# - média entre 5.0 e 6.9: RECUPERAÇÃO
# - média 7.0 ou superior: APROVADO
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1+n2)/2

if m >= 7:
    print(f'Aprovado.')
elif m >= 5:
    print(f'Recuperação.')
else:
    print(f'Reprovado.')
