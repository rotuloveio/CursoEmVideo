# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostra:
# - quantos números foram digitados.
# - a lista de valores, ordenada de forma decrescente.
# - se o valor 5 foi digitado e está ou não na lista.
nums = list()
while True:
    nums.append(int(input('Digite um valor: ')))
    resp = ''
    while resp != 'S' and resp != 'N':
        resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break

nums.sort(reverse=True)

print(f'Você digitou {len(nums)} valor(es)')
print(f'Ordem decrescente: {nums}')
print('5 está na lista.' if 5 in nums else '5 não está na lista.')
