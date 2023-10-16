# Exercícios com funções
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplicação(*args):
    total = 1
    for numero in args:
       
         total = total * numero
    return total

multiplicação = multiplicação(1,2,8,10,20,32)

print(multiplicação)

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)

def juros_compostos(principal, taxa, tempo):
    montante = principal * (1 + taxa) ** tempo
    return montante

print(juros_compostos(1000, 0.011, 12))


