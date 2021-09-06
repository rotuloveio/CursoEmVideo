# Aprimore o DESAFIO 086, mostrando no final:
# - a soma de todos os valores pares digitados.
# - a soma dos valores da terceira coluna.
# - o maior valor da segunda linha.
matriz = [
    [],
    [],
    []
]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite o valor da célula [{i}, {j}]: ')))

print('-=' * 20)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end='')
    print()

print('-=' * 20)

somacol = somapar = 0

for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
        if j == 2:
            somacol += matriz[i][j]

print(f'A soma dos pares é {somapar}.')
print(f'A soma da terceira coluna é {somacol}.')
print(f'O maior valor da 2ª linha é {max(matriz[1])}.')
