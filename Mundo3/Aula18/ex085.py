# Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescrente.
nums = [[], []]

for i in range(0, 7):
    num = int(input(f'Digite o {i + 1}º valor: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)

nums[1].sort()
nums[0].sort()

print(f'Os pares são: {nums[0]}')
print(f'Os ímpares são: {nums[1]}')
