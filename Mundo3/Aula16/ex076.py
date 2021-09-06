# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados de forma tabular.
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-'*30)
for pos, obj in enumerate(lista):
    if pos % 2 == 0:
        print(f'{obj:.<21}R$ ', end='')
    else:
        print('{: >6.2f}'.format(obj))
print('-'*30)