# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
g=''
while g != 'M' and g != 'F':
    g = input('Digite seu sexo [M/F]: ').upper()
