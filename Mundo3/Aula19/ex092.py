# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se
# por acaso a CTPS for diferente de 0, o dicionário receverá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

agora = date.today().year

pessoa = dict(
    Nome=input('Nome: '),
    Idade=agora - int(input('Ano de nascimento: ')),
    CTPS=int(input('CTPS [0 = não tem]: '))
)

if pessoa['CTPS']:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + 35 - (agora - pessoa['Contratação'])

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}.')
