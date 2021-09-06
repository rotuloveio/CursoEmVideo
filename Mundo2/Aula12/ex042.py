# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - equilátero: todos os lados iguais
# - isósceles: dois lados iguais
# - escaleno: todos os lados diferentes
print('\033[1;32m-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 and r2 == r3:
        print('Podem formar um triângulo equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Podem formar um triângulo isósceles.')
    else:
        print('Podem formar um triângulo escaleno.')
else:
    print('Não podem formar um triângulo.')
