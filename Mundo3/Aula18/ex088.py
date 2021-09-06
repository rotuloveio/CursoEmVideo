# Faça um programa que ajude um jogador da Mega Sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
# tudo em uma lista composta.
from random import randint
from time import sleep

qtd = int(input('Quantos jogos? '))

jogos = list()
jogo = list()

for cont in range(0, qtd):
    del jogo
    jogo = list()
    for j in range(0, 6):
        num = randint(1, 60)
        while num in jogo:
            num = randint(1, 60)
        jogo.append(num)
    jogo.sort()
    jogos.append(jogo[:])
    print(f'Jogo {cont + 1}: {jogos[cont]}')
    sleep(1)
