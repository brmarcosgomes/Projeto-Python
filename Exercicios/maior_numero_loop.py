"""
Faça um programa que leia 5 números e informe o maior número.
"""
rep = range(5) 
maior_numero = 0
numero = 0

for num in rep:
    numero = int(input(f"Digite um o {num+1}: "))
    
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior numero é {maior_numero}")