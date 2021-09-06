# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input("Digite um número para ver sua tabuada [digite um número negativo p/ parar]: "))
    if n < 0:
        break
    print('-' * 12)
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
    print('-' * 12)
