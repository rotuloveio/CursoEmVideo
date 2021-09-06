# Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários.
import random
num = random.randint(0, 10)
guess = 11
tries = 0
while guess != num:
    guess = int(input("Adivinhe o número de 0 a 10: "))
    tries += 1
    if guess < num:
        print('Mais... tente outra vez.')
    if guess > num:
        print('Menos... tente outra vez.')

print(f'Você acertou em {tries} tentativa(s).')
