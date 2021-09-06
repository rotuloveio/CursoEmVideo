def linha(tam=40):
    print('-' * tam)


def titulo(msg, tam=40):
    linha()
    print(f'{msg:^{tam}}')
    linha()


def leiaint(msg):
    while True:
        n = input(msg)
        try:
            return int(n)
        except:
            print('\033[31mERRO: por favor, digite um valor inteiro válido\033[m')


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    linha()
    return leiaint('\033[32mSua Opção: \033[m')


def cadastro():
    titulo('NOVO CADASTRO')
    file = open('cadastro.txt', 'a')
    nome = input('Nome: ')
    while True:
        try:
            idade = int(input('Idade: '))
        except ValueError:
            print(f'\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            break
    print(f'{nome:30}{idade} anos', end='\n', file=file)
    print(f'Novo registro de {nome} adicionado.')
    file.close()


def mostra():
    titulo('PESSOAS CADASTRADAS')
    file = open('cadastro.txt', 'r')
    for line in file.readlines():
        print(line, end='')
    file.close()
