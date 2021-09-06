# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.
jogadores = []
while True:
    jogador = dict(Nome=input('Nome: '),
                   Partidas=int(input('Partidas jogadas: ')))

    gols = []

    total = 0

    for cont in range(0, jogador['Partidas']):
        gols.append(int(input(f'Quantos gols ele fez na {cont+1}ª partida: ')))

    for gol in gols:
        total += gol

    jogador['Gols'] = gols[:]
    jogador['Total'] = total

    jogadores.append(jogador.copy())

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').upper()[0]
    if resp == 'N':
        break

print('-' * 40)
print(f'cod nome       gols            total')

for index, jogador in enumerate(jogadores):
    print(f'{index:>3} {jogador["Nome"]:<10} {str(jogador["Gols"]):<15} {jogador["Total"]}')

while True:
    print('-' * 40)
    index = int(input('Mostrar dado de qual jogador? [999 p/ parar] '))
    if index == 999:
        break
    if index < 0 or index >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {index}! Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[index]["Nome"]} --')
        for j in range(0, jogadores[index]["Partidas"]):
            print(f'   No {j+1}º jogo fez {jogadores[index]["Gols"][j]} gol(s).')
        print(f'Um total de {jogadores[index]["Total"]} gol(s).')

print('VOLTE SEMPRE!')
