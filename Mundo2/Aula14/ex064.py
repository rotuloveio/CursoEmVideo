# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num = soma = 0
total = -1
while num != 999:
    soma += num
    total += 1
    num = int(input('Digite um número [999 p/ sair]: '))

print(f'Você digitou {total} termo(s) e seu somatório é {soma}.')
