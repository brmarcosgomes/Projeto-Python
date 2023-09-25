ano = input("Escreva o ano que deseja analisar: ")
int_ano = int(ano)

if int_ano % 4 == 0 and int_ano % 100 != 0 or int_ano % 400 == 0:
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")
