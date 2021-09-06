def aumentar(preco=0, taxa=0, formato=False):
    if formato:
        return moeda(preco * (1 + taxa / 100))
    return preco * (1 + taxa / 100)


def diminuir(preco=0, taxa=0, formato=False):
    if formato:
        return moeda(preco * (1 - taxa / 100))
    return preco * (1 - taxa / 100)


def dobro(preco=0, formato=False):
    if formato:
        return moeda(preco * 2)
    return preco * 2


def metade(preco=0, formato=False):
    if formato:
        return moeda(preco / 2)
    return preco / 2


def moeda(valor=0.0, tipo='R$'):
    return f'{tipo}{valor:.2f}'.replace('.', ',')


def resumo(preco, aumento=10, reducao=10):
    print('-' * 30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('-' * 30)
    print(f'Preço analisado: {moeda(preco)}')
    print(f'Dobro do preço:  {dobro(preco, True)}')
    print(f'Metade do preço: {metade(preco, True)}')
    print(f'{aumento}% de aumento:  {aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução:  {diminuir(preco, reducao, True)}')
    print('-' * 30)
