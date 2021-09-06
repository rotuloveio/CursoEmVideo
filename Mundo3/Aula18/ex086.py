# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [
    [],
    [],
    []
]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(input(f'Digite o valor da célula [{i}, {j}]: '))

print('-=' * 20)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end='')
    print()
