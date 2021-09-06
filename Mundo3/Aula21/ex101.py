# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
from datetime import date


def voto(ano):
    idade = date.today().year - ano
    resp = f'Com {idade} anos: '
    if idade < 16:
        resp += 'NÃO VOTA'
    elif idade < 18 or idade >= 65:
        resp += 'VOTO OPCIONAL'
    else:
        resp += 'VOTO OBRIGATÓRIO'
    return resp


print(f'{voto(int(input("Em que ano você nasceu? ")))}')
