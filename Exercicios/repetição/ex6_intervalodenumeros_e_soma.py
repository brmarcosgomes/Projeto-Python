#Faça um programa que receba dois números inteiros
#e gere os números inteiros que estão no intervalo compreendido por eles.

def numeros_inteiros (num_inicial, num_final):
    for i in range(num_inicial, num_final):
        print (i)

def soma_inteiros (num_inicial, num_final):
    soma = 0
    for i in range(num_inicial, num_final):
        i += i
        #soma = i    
    print (i)

numeros_inteiros(0, 11)
soma_inteiros(0, 11)