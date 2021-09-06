def aumentar(valor, taxa, formato=False):
    if formato:
        return moeda(valor * (1 + taxa / 100))
    return valor * (1 + taxa / 100)


def diminuir(valor, taxa, fomato=False):
    if fomato:
        return moeda(valor * (1 - taxa / 100))
    return valor * (1 - taxa / 100)


def dobro(valor, formato=False):
    if formato:
        return moeda(valor * 2)
    return valor * 2


def metade(valor, formato=False):
    if formato:
        return moeda(valor / 2)
    return valor / 2


def moeda(valor=0, tipo='R$'):
    return f'{tipo}{valor:.2f}'.replace('.', ',')


def resumo(valor, aumento=10, reducao=10):
    print('-' * 30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('-' * 30)
    print(f'Preço analisado: {moeda(valor)}')
    print(f'Dobro do preço:  {dobro(valor, True)}')
    print(f'Metade do preço: {metade(valor, True)}')
    print(f'{aumento}% de aumento:  {aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução:  {diminuir(valor, reducao, True)}')
    print('-' * 30)
