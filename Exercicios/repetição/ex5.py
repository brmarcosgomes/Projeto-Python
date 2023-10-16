#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

def numeros_impares(b, f):
    for i in range(b, f):
        if (i % 2 != 0):
            print(i)

def numeros_pares(b, f):
    for i in range(b, f):
        if (i % 2 == 0):
            print(i)

numeros_impares(1, 50)
numeros_pares(1, 50)
