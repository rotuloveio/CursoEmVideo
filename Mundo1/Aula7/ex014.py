# Escreva um programa que leia uma temperatura digitada em ºC e converta para ºF.
c = float(input("Informe a temperatura em ºC: "))
f = c * 9 / 5 + 32
print(f"A temperatura de {c}ºC corresponde a {f:.1f}ºF.")
