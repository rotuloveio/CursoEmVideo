# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada km acima do limite.
vel = int(input('Velocidade [km/h]: '))
if vel > 80:
    print(f'Você foi multado em R${7*(vel-80):.2f}.')
else:
    print('Tenha um bom dia! Dirija com segurança!')
