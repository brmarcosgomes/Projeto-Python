"""

PT 1----------------------------------------------
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

PT2-------------------------------------------
Calculo do segundo dígito do CPF
CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf = "50423314840"


numeros_cpf = ""
lista_CPF = []
resultado_multiplicacao = []
resultado_multiplicacao2 = []


for caractere in cpf:

    if caractere.isdigit():
        numeros_cpf += caractere

for numeros in numeros_cpf:
    lista_CPF.append(numeros)
    lista_9_digitos_CPF_int = [int(x) for x in lista_CPF]

cpf_usuario = lista_9_digitos_CPF_int[0:9]
List_first_digit = lista_9_digitos_CPF_int[0:9]
List_second_digit = lista_9_digitos_CPF_int[0:10]

for indice, item in enumerate(List_first_digit):
    multiplicador = 10 - indice
    resultado = item * multiplicador
    resultado_multiplicacao.append(resultado)
    #print(f"{item} * {multiplicador} = {resultado}")

validador_primeiro_digito = (sum(resultado_multiplicacao) * 10) % 11

for indice, item in enumerate(List_second_digit):
    multiplicador = 11 - indice
    resultado = item * multiplicador
    resultado_multiplicacao2.append(resultado)
    #print(f"{item} * {multiplicador} = {resultado}")

validador_segundo_digito = (sum(resultado_multiplicacao2) * 10) % 11


validador_primeiro_digito = 0  if validador_primeiro_digito > 9 else validador_primeiro_digito 
validador_segundo_digito = 0 if validador_segundo_digito > 9 else validador_segundo_digito
ultimo_e_penultimo_digito = [validador_primeiro_digito, validador_segundo_digito]
cpf_usuario.extend(ultimo_e_penultimo_digito)
validador_cpf = True if lista_9_digitos_CPF_int == cpf_usuario else False

print(f"CPF: {cpf}")
print(f"O resultado do primeiro digito é {validador_primeiro_digito}")
print(f"O resultado do segundo digito é {validador_segundo_digito}")

print(lista_9_digitos_CPF_int)
print(cpf_usuario)
print(validador_cpf)









