# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
d = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
print(f'O total a pagar é de R${d * 60 + km * .15:.2f}.')
