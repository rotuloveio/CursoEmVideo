# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disse, crie duas listar extras que vão conter apenas os valores pares e ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
nums = list()
while True:
    nums.append(int(input('Digite um valor: ')))
    resp = ''
    while resp != 'S' and resp != 'N':
        resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break

pares = []
impares = []

for num in nums:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Os números são: {nums}')
print(f'Os pares são: {pares}')
print(f'Os ímpares são: {impares}')
