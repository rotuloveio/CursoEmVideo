# Reescreva a função leiaint() do DESAFIO 104, incluindo agora possibilidade da digitação de um número de tipo inválido
# Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.
def leiaint(msg):
    while True:
        n = input(msg)
        try:
            return int(n)
        except:
            print('\033[31mERRO: por favor, digite um valor inteiro válido\033[m')


def leiafloat(msg):
    while True:
        n = input(msg)
        try:
            return float(n)
        except:
            print('\033[31mERRO: por favor, digite um valor real válido\033[m')


print(f'O valor inteiro digitado foi {leiaint("Digite um número inteiro: ")} '
      f'e o valor real digitado foi {leiafloat("Digite um número real: ")}')
