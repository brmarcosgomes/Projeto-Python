#Faça um Programa que leia três números e mostre o maior e o menor deles.
print("Maior e Menor numero")
num1 = input("Digite o primeiro numero:")
num2 = input("Digite o segundo numero:")
num3 = input("Digite o terceiro numero:")

int_num1 = int(num1)
int_num2 = int(num2)
int_num3 = int(num3)

if num1 > num2 > num3:
    print(f"Numero 1: {int_num1}")
    print(f"Numero 2: {int_num2}")
    print(f"Numero 3: {int_num3}")
    print(f"O maior numero é o {int_num1}")
    print(f"O menor numero é o {int_num3}")
elif num2 > num1 > num3:
    print(f"Numero 1: {int_num1}")
    print(f"Numero 2: {int_num2}")
    print(f"Numero 3: {int_num3}")
    print(f"O maior numero é o {int_num2}")
    print(f"O menor numero é o {int_num3}")
elif num3 > num1 > num2:
    print(f"Numero 1: {int_num1}")
    print(f"Numero 2: {int_num2}")
    print(f"Numero 3: {int_num3}")
    print(f"O maior numero é o {int_num3}")
    print(f"O menor numero é o {int_num2}")
elif num1 > num3 > num2:
    print(f"Numero 1: {int_num1}")
    print(f"Numero 2: {int_num2}")
    print(f"Numero 3: {int_num3}")
    print(f"O maior numero é o {int_num1}")
    print(f"O menor numero é o {int_num2}")
elif num2 > num3 > num1:
    print(f"Numero 1: {int_num1}")
    print(f"Numero 2: {int_num2}")
    print(f"Numero 3: {int_num3}")
    print(f"O maior numero é o {int_num2}")
    print(f"O menor numero é o {int_num1}")
elif int_num3 > int_num2 > int_num1:
    print(f"Numero 1: {int_num1}")
    print(f"Numero 2: {int_num2}")
    print(f"Numero 3: {int_num3}")
    print(f"O maior numero é o {int_num3}")
    print(f"O menor numero é o {int_num1}")



