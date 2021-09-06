# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# - até 9 anos: MIRIM
# - até 14 anos: INFANTIL
# - até 19 anos: JUNIOR
# - até 25 anos: SÊNIOR
# - acima: MASTER
from datetime import date

ano = int(input('Ano de nascimento: '))
agora = date.today().year

idade = agora - ano

if idade > 25:
    print(f'Master.')
elif idade > 19:
    print(f'Sênior.')
elif idade > 14:
    print(f'Junior.')
elif idade > 9:
    print(f'Infantil.')
else:
    print(f'Mirim.')
