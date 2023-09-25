#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Escreva seu nome: ")
senha = input("Senha: ")

while nome == senha:
    print("Valor invalido!")
    print("Nome e senha iguais, os valores devem ser diferentes!")
    nome = input("Escreva seu nome: ")
    senha = input("Senha: ")

print(f"Usuario: {nome}")
print(f"Senha: {senha}")