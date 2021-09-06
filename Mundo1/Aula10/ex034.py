# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Salário: R$'))

if sal > 1250:
    print(f'Aumento: R${sal * .1:.2f}')
else:
    print(f'Aumento: R${sal * .15:.2f}')
