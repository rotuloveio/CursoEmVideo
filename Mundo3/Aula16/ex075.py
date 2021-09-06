# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# - quantas vezes apareceu o valor 9.
# - em que posição foi digitado o primeiro valor 3.
# - quais foram os números pares.
nums = (int(input('Digite um valor: ')),
        int(input('Digite outro valor: ')),
        int(input('Digite mais um valor: ')),
        int(input('Digite o último valor: ')))

if nums.count(9):
    print(f'O número 9 apareceu {nums.count(9)} vez(es).')
else:
    print('O número 9 não apareceu.')
if 3 in nums:
    print(f'O primeiro 3 está na {nums.index(3)}ª posição.')
else:
    print('O número 3 não apareceu.')
print('Os números pares foram: ', end='')
for pos, i in enumerate(nums):
    if i % 2 == 0:
        print(i, end=' ')
