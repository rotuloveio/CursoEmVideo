# Crie uma tupla preenchida com os 20 clubes do brasileirão, na ordem de colocação.
# Depois mostre:
# - os 5 primeiros.
# - os 4 últimos.
# - os times em ordem alfabética.
# - em que posição está a Chapecoense
bra = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino',
       'Flamengo', 'Athletico-PR', 'Atlético-GO', 'Ceará',
       'Internacional', 'Santos', 'Corinthians', 'Juventude',
       'Bahia', 'São Paulo', 'Fluminense', 'Cuiabá',
       'Sport Recife', 'América-MG', 'Grêmio', 'Chapecoense')

for i in range(0, 5):
    print(f'{i+1}º colocado: {bra[i]}')

for i in range(16, 20):
    print(f'{i+1}º colocado: {bra[i]}')

print(sorted(bra))

print(f"A Chapecoense está no {bra.index('Chapecoense')+1}º lugar.")
