# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

def um_a_vinte (n):
    for i in range(1, n+1):
        print (i, end=" ")
        i += n
        
um_a_vinte(20)