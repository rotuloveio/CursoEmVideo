# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se
# será mostrado ou não na tela o processo de cálculo do fatorial
def fatorial(n=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o cálculo.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if c != 1 and show:
            print(f'{c} x ', end='')
        if c == 1 and show:
            print(f'{c} = ', end='')
    return f


print(fatorial(5, True))
