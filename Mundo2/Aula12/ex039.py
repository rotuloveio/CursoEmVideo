# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também
# deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano = int(input('Ano de nascimento: '))
agora = date.today().year
idade = agora - ano

if idade == 18:
    print(f'Você deve se alistar.')
elif idade > 18:
    print(f'Você devia ter se alistado a {idade - 18} ano(s) atrás.')
else:
    print(f'Você deverá se alistar daqui a {18 - idade} ano(s).')
