"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Escreva seu nome: ")
nome_num = len(nome)

if nome_num <= 4:
    print("Seu nome é curto")
elif nome_num >= 5 and nome_num <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é grande")
