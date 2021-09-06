# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
p = float(input('Preço: R$'))
print('Condição de pgto:')
print('1 - à vista no dinheiro/cheque')
print('2 - à vista no cartão')
print('3 - em até 2x no cartão')
c = int(input('4 - em 3x/+ no cartão\n'))

print('Total a pagar:')
if c == 1:
    print(f'R${p*.9:.2f}')
elif c == 2:
    print(f'R${p*.95:.2f}')
elif c == 3:
    print(f'R${p:.2f}')
else:
    print(f'R${p*1.2:.2f}')
