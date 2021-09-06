# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# Solução copiada da resolução
from random import randint
from time import sleep
from operator import itemgetter
dados = {}

print('Valores sorteados:')

for i in range(0, 4):
    dados[f'Jogador {i+1}'] = randint(1, 6)

for k, v in dados.items():
    print(f'    O {k} tirou {v}.')
    sleep(1)

print('Ranking:')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)

for i in range(0, 4):
    print(f'    {i+1}° colocado: {ranking[i][0]} com {ranking[i][1]}')
