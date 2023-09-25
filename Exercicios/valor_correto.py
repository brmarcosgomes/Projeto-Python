#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e 
#continue pedindo até que o usuário informe um valor válido.

nota = input("Escreva um nota de zero a dez: ")
#int_nota = int(nota)
int_nota_escolhida = "7"

while nota != int_nota_escolhida:
    print ("Valor invalido!")
    nota = input("Escolha outro valor: ")

print("Valor correto!")