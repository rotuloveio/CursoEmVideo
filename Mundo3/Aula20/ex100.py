# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a some entre
# todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep


def sorteia(nums):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        sleep(.5)
        n = randint(1, 10)
        nums.append(n)
        print(n, end=' ')
    print('PRONTO!')


def somapar(nums):
    soma = 0
    for num in nums:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {nums}, temos {soma}.')


num = list()
sorteia(num)
somapar(num)
