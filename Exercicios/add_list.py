


lista_nomes = ['Marcos', 'Leonardo', 'Matheus', 'Enzo', 'Alan', 'Raffa', 'Ju']

desejo = input("Deseja adicionar um nome a lista?")
    
while desejo == "s":
   
    lista_nomes.append (input("Adionar nome na lista: "))
    print(lista_nomes)
    sair = input("DEseja adicionar outro nome na lista?  S ou N")
    
    if sair == "n":
        break

print(lista_nomes.index("u"))



        




