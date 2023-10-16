#Faça um programa que leia 5 números e informe a soma e a média dos números.

def media_numero(n):
    soma = int(0)
    for i in range(n):
        numero = int(input("Escreva um numero: "))
        soma += numero
        media = soma/n
    print(f"A media dos {n} numeros é: {media}") 

media_numero(5)