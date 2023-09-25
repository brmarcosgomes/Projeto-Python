"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input("Digite um numero inteiro: ")

try:
    numero1 = int(numero)
    if numero1 % 2 == 0:
        print("O numero é par")
    else:
            print("")

except:
    print("Não é inteiro ou não é numero!")