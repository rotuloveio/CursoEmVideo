# Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no DESAFIO 108.
from moeda import *

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando 10%, temos {aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {diminuir(p, 13, True)}')
