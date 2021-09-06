# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
nums = list()

for cont in range(0, 5):
    num = int(input('Digite um número: '))
    if cont == 0:
        nums.append(num)
        print('Adicionado ao final da lista...')
    else:
        for index in range(0, cont):
            if nums[index] > num:
                nums.insert(index, num)
                print(f'Adicionado na posição {index} da lista...')
                break
            elif index == cont - 1:
                nums.append(num)
                print('Adicionado ao final da lista...')

print(f'A lista em ordem é {nums}')
