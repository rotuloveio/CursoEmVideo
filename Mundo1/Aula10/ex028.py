# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deve escrever na tela se o usuário venceu ou perdeu.
import random
num = random.randint(0, 5)
guess = input("Adivinhe o número de 0 a 5: ")
print('Acertou!' if guess == num else f'Errou, o número era {num}.')
