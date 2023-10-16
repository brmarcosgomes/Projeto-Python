#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def factorial_number(n):
    a = n 
    for i in range (n - 1): # O numero dentro de range só mostra quantas vezes ele vai rodar não altera nada.
        n = n - 1  
        a = a * n
    print (a)

def factorial_number_Oficial(n):
    a = 1
    for i in range (n):
        a = a * (i + 1)      
    print (a)
      
factorial_number(5)
factorial_number_Oficial(5)

