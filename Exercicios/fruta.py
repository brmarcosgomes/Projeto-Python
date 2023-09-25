""" 
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                            Até 5 Kg           Acima de 5 Kg
        Maçã          R$ 1,80 por Kg          R$ 1,50 por Kg
        Morango       R$ 2,50 por Kg          R$ 2,20 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) 
de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

nome = input("Qual seu nome?")
quantidade_maca = input("%s, qual a quantidade de Maça que deseja? (KG)" % (nome))
quantidade_morango = input("%s, qual a quantidade de morango que deseja? (KG)" % (nome))
f_quantidade_maca = float(quantidade_maca)
f_quantidade_morango = float(quantidade_morango)
valor_maca = 0
valor_morango = 0
total_pagar = 0
Desconto_total_pagar = 0
valor_final = 0



if f_quantidade_maca >= 5:
    valor_maca = f_quantidade_maca * 1.5
else:
    valor_maca = f_quantidade_maca * 1.8

if f_quantidade_morango >= 5:
    valor_morango = f_quantidade_maca * 2.2
else:
    valor_morango = f_quantidade_morango * 2.5

total_pagar = valor_maca + valor_morango

if f_quantidade_maca + f_quantidade_morango >= 8 or total_pagar >= 25:
    Desconto_total_pagar = total_pagar * 0.10
    valor_final = total_pagar - Desconto_total_pagar
    print(f"Valor Total: {total_pagar}")
    print(f"Desconto: {Desconto_total_pagar}")
    print(f"Valor Total: {valor_final}")
else:
    Desconto_total_pagar = 0
    valor_final = total_pagar
    print(f"Valor Total: {total_pagar}")
    print(f"Desconto: {Desconto_total_pagar}")
    print(f"Valor Total: {valor_final}")
    print(total_pagar)











