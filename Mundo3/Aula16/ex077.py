# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'As vogais em \033[31m{palavra}\033[m são: ', end='')
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            print(f'\033[31m{letra}\033[m', end=' ')
    print()
