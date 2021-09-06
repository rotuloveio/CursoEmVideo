# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por
# km para viagens de até 200km e R$0,45 para viagens mais longas
d = int(input('Distância [km]: '))
if d <= 200:
    print(f'Preço: R${d*.5:.2f}')
else:
    print(f'Preço: R${d*.45:.2f}')
