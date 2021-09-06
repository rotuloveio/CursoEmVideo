# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*nums):
    print('-=' * 40)
    print('Analisando os valores passados...')
    for num in nums:
        sleep(.5)
        print(num, end=' ')
        sleep(.5)
    print(f'\n{len(nums)} valor(es) informado(s).')
    print('O maior valor passado foi ', end='')
    if len(nums):
        print(f'{max(nums)}.')
    else:
        print('0.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
