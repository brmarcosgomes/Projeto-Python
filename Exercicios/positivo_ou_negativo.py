num = input("Escreva um numero para saber se é negativo ou positivo: ")
int_num = int(num)

if int_num > 0:
    print("O numero é positivo")
elif int_num < 0:
    print("O numero é negativo")
else:
    print("O numero é 0")