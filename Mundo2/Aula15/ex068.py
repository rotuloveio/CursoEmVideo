# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no
# final do jogo.
from random import randint

v = 0

while True:
    pl = ''
    while pl != 'P' and pl != 'I':
        pl = input('Par ou Ímpar? [P/I] ').upper().strip()
    npl = -1
    while npl < 0 or npl > 5:
        npl = int(input('Quantos dedos? [0 - 5] '))
    pc = randint(0, 5)
    soma = npl + pc
    if (pl == 'I' and soma % 2 == 0) or (pl == 'P' and soma % 2 == 1):
        break
    print(f'Você jogou {npl} e o pc jogou {pc}. A soma deu {soma} e você venceu.')
    v += 1

print(f'Você jogou {npl} e o pc jogou {pc}. A soma deu {soma} e você perdeu.')
print(f'Você venceu {v} vez(es).')
