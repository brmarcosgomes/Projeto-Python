def lista_n ():
    lista = []
    for i in range(5):
        num = (input("Adicione um numero na lista: "))
        lista.append(num)
    return lista


def lista_inversa(n):
    lista = n[::-1]
    lista_invertida = lista
    return lista_invertida

lista = lista_n()
print(lista)
listainv = lista_inversa(lista)
print(listainv)

