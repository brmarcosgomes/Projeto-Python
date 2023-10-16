

for i in range(10):
    temperatura = float(input("Digite a temperatura: "))
    maior = float('inf')
    menor = float('-inf')
    if temperatura > maior:
                maior = temperatura
    if temperatura < menor:
                menor = temperatura

print("A maior temperatura é: ", maior)
print("A menor temperatura é: ", menor)