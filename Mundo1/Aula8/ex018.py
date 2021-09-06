# Faça um programa que leia um ângulo qualquer e mostre na tela os valores de seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Ângulo: '))

sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)

print(f'O seno é {sen}, o cosseno é {cos} e a tangente é {tan}.')
