#Faça um programa que leia 5 números e informe o maior número.

def maior_numero():
    numero = int(0)
    maior = int(0)
    for i in range(5):
        numero = int(input("Escreva um numero: "))
        if numero > maior:
            maior = numero
    print(maior) 

maior_numero()
