# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá por extenso.
nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
        num = -1
        while num < 0 or num > 20:
                num = int(input('Escolha um número de 0 a 20: '))

        print(f"Você digitou {nums[num]}.")

        resp = ''
        while resp != 'S' and resp != 'N':
                resp = input('Você quer continuar? [S/N] ').upper()

        if resp == 'N':
                break
