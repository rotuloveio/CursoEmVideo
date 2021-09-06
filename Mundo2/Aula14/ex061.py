# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
n1 = int(input('Digite o primeiro termo da PA: '))
ra = int(input('Digite a razão da PA: '))

t = 0
while t < 10:
    print(n1+t*ra)
    t += 1
