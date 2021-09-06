# Escreva um programa que leia um número n inteiro e mostre na tela os n primeiros elementos da Sequência de Fibonacci.
termos = int(input('Quantos termos da sequência de Fibonacci você quer mostrar? '))

cont = atual = penultimo = 0
anterior = 1
while cont < termos:
    print(f'{atual}', end=' ')
    atual = anterior + penultimo
    penultimo = anterior
    anterior = atual
    cont += 1
