# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
s = 0
val = 0
for i in range(3, 501, 3):
    if i % 2:
        s += i
        val += 1
print(f'A soma de todos os {val} valores solicitados é {s}.')
