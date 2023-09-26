"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
Altere o programa anterior para mostrar no final a soma dos números.
"""

num1 = int(12)
num2 = int(20)
soma = 0
while num1 <= num2:
    print(num1)
    num1 += 1
    soma += num1 

print(soma)