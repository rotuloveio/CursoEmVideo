# Crie um programa que leia dois números e mostre:
# - a soma entre eles
# - o produto entre eles
# - a divisão (simples) entre eles
# - a divisão inteira entre eles
# - a potência de n1 em n2
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
print(f"A soma entre {n1} e {n2} vale {n1+n2}.")
print(f"O produto entre {n1} e {n2} vale {n1*n2}.")
print(f"A divisão entre {n1} e {n2} vale {n1/n2:.3f}.")
print(f"A divisão inteira entre {n1} e {n2} vale {n1//n2}.")
print(f"A potência de {n1} em {n2} vale {n1**n2}.")
