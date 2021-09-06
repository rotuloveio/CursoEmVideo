# Faça um programa que leia os comprimentos do cateto oposto e do cateto adjacento de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
print(f'A hipotenusa é {(co**2+ca**2)**.5}.')
