# Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, dm, cm e mm.
n1 = float(input("Distância em metros: "))
print(f"A medida de {n1}m corresponde a:")
print(f"{n1/1000} km")
print(f"{n1/100} hm")
print(f"{n1/10} dam")
print(f"{n1*10:.0f} dm")
print(f"{n1*100:.0f} cm")
print(f"{n1*1000:.0f} mm")
