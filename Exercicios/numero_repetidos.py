#Faça um programa que imprima na tela os números de 1 a 20, 
#um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

num_inicial = 0
num_final = 20


while num_inicial <= num_final:
    print(num_inicial)
    num_inicial += 1
while num_inicial <= num_final:
    print(num_inicial, end=" ")
    num_inicial += 1
    