"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: ")
idade = input(f"{nome}, digite sua idade: ")
#nome_invertido = nome (::-1)
nome_num = len(nome)
print(nome)
print(idade)
#espaço = len(nome, " ")

if nome and idade:
    print(f"Seu nome é:{nome}")
    print("Seu nome invertido é: %s" % nome[::-1])
    
    if " " in nome:
        print(f"Seu nome contém espaços")
    else:
        print(f"Seu nome não contém espaços")
    
    print(f"Seu nome contém {nome_num} letras")
    print("A primeira letra do seu nome é: %s" % nome[0])
    print("A ultima letra do seu nome é:  %s" % nome[-1])
else:
    print("Desculpe, voce deixou o campos vazios")