# Crie um programa que gerencia o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict(Nome=input('Nome: '),
               Partidas=int(input('Partidas jogadas: ')))

gols = []

total = 0

for part in range(0, jogador['Partidas']):
    gols.append(int(input(f'Quantos gols ele fez na {part+1}ª partida: ')))

for gol in gols:
    total += gol

jogador['Gols'] = gols[:]
jogador['Total'] = total

print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partida(s).')
for part in range(0, jogador['Partidas']):
    print(f'    Na {part + 1}ª partida, fez {gols[part]} gol(s).')
print(f'Foi um total de {jogador["Total"]} gol(s) em {jogador["Partidas"]} partida(s).')
