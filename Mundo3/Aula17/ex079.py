# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, seráo exibidos todos os valores únicos digitados, em ordem crescente.
n = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in n:
        n.append(num)
        print(f'{num} adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    resp = ''
    while resp != 'S' and resp != 'N':
        resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break

n.sort()

print(f'Você digitou os valores {n}')
