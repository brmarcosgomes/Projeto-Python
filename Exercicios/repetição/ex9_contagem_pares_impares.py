#Faça um programa que peça 10 números inteiros,
#calcule e mostre a quantidade de números pares e a quantidade de números impares.

def contagem_pares_impares():
    number = 0
    pares = 0 
    impares = 0 
    for i in range(10):
        number = int(input("Digite um número: "))
        if number % 2 == 0:
            pares = pares + 1
        elif number % 2 != 0:
            impares = impares + 1
    
    print(f"Quantidade de pares: {pares}")
    print(f"Quantidade de impares: {impares}")

contagem_pares_impares()

