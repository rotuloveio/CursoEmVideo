# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mosgtre seu status, de acordo com a
# tabela abaixo:
# - abaixo de 18.5: abaixo do peso
# - entre 18.5 e 25: peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: obesidade
# - acima de 40: obesidade mórbida
peso = float(input('Peso em kg: '))
h = float(input('Altura em m: '))

imc = peso / h**2

if imc > 40:
    print('Obesidade mórbida.')
elif imc >= 30:
    print('Obesidade.')
elif imc >= 25:
    print('Sobrepeso.')
elif imc >= 18.5:
    print('Peso ideal.')
else:
    print('Abaixo do Peso.')
