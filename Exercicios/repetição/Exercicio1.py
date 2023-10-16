# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:

    nota = input("Digite uma nota de 0 a 10: ")
    notaint = int(nota)

    if notaint < 0 or notaint > 10:
        print("Valor invalido! ")
        continue
    else:
        print(notaint)
        break

    


