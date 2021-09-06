# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa encerrará.
# OBS: use cores.
from time import sleep


def sand(msg, cor):
    tam = len(msg) + 4
    print(f'{cor}~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print('\033[m', end='')
    sleep(1)


def ajuda(msg):
    sand(f"Acessando o manual do comando '{msg}'", '\033[30:44m')
    print('\033[7:40m', end='')
    help(msg)
    print('\033[m', end='')
    sleep(2)


while True:
    sand('SISTEMA DE AJUDA PyHELP', '\033[30:42m')
    f = input('Função ou Biblioteca > ').strip()

    if f.upper() == 'FIM':
        break

    ajuda(f)

sand('ATÉ LOGO', '\033[45m')
