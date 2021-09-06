# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário.
val = float(input('Qual valor da casa? '))
sal = float(input('Qual seu salário? '))
ano = float(input('Em quantos anos? '))

parcela = val / (ano * 12)

limite = sal * 0.3

if parcela > limite:
    print('Negado.')
else:
    print('Aprovado.')
