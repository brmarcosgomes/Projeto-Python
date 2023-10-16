# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

def verification_name(name, password):
   
    while name == password:
        print("Valor invalido")
        print("Senha e Usuario são iguais")
        name = input("Digite outro nome: ")
        password = input("Digite outra senha: ")
        if name != password:
            break
        else:
            continue
 
    


Username = input("Digite o nome de Usuario")
password = input("Digite a senha")
verification_name(Username, password)






    
