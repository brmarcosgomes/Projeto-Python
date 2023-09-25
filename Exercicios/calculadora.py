#Calculadora 
#tipo_conta = ""
#sistema = True
while True:

    tipo_conta = input("Qual tipo de conta deseja fazer? \n[+] - operacao\n[-] - Subtração\n[*] - Multiplicação\n[/] - Divisão\n")
    num_1 = 0
    num_2 = 0
    operacao = 0
    if tipo_conta == "+":
        num_1 = input("Digite o Primeiro valor a ser soma: ")
        num_2 = input("Digite o Segundo valor a ser soma: ")
        operacao = float(num_1) + float(num_2)
        print(f"A operacao dos valores é {operacao}")
        #continue
    elif tipo_conta == "-":
        num_1 = input("Digite o Primeiro valor a ser subtraido: ")
        num_2 = input("Digite o Segundo valor a ser subtraido: ")
        operacao = float(num_1) - float(num_2)
        print(f"A operacao dos valores é {operacao}")
        #continue
    elif tipo_conta == "*":
        num_1 = input("Digite o Primeiro valor a ser multiplicado: ")
        num_2 = input("Digite o Segundo valor a ser multiplicado: ")
        operacao = float(num_1) * float(num_2)
        print(f"A operacao dos valores é {operacao}")
        #continue
    elif tipo_conta == "/":
        num_1 = input("Digite o Primeiro valor a ser dividido: ")
        num_2 = input("Digite o Segundo valor a ser dividido: ")
        operacao = float(num_1) / float(num_2)
        print(f"A operacao dos valores é {operacao}")
        #continue
    else:
        print("Operador Invalido")

    sair = input('Deseja realizar outra operação? [s]Sim: [n]Não:')

    if sair == "s":
        continue
    else:
        break
