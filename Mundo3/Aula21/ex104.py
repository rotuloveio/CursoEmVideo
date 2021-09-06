# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python, só
# que fazendo a validação para aceitar apenas um valor numérico.
def leiaint(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            return int(num)
            break
        else:
            print('\033[31mDigite um número inteiro válido.\033[m')


print(f'Você acabou de digitar o número {leiaint("Digite um número: ")}.')
