# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa envcerra quando ele disser que quer mostrar 0 termos.
n1 = int(input('Digite o primeiro termo da PA: '))
ra = int(input('Digite a razão da PA: '))

t = 0
lim = 10
while t < lim:
    print(n1+t*ra, end=' ')
    t += 1
    if t == lim:
        lim += int(input('\nQuantos termos a mais mostrar? '))
