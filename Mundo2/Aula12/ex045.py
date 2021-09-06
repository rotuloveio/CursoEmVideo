# Crie um programa que faça o computador jogar jokenpô com você.
import random

jokenpo = ['pedra', 'papel', 'tesoura']
while 1:
    pl = input('Digite pedra, papel ou tesoura: ')
    pc = random.choice(jokenpo)

    print(f'PC: {pc} x PLAYER: {pl}')

    if pc == pl:
        print('Empate.')
    elif(pc == 'pedra' and pl == 'tesoura') or (pc == 'tesoura' and pl == 'papel') or (pc == 'papel' and pl == 'pedra'):
        print('Computador venceu.')
    else:
        print('Você venceu.')
