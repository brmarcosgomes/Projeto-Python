"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país 
A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.


pais_a = 80000
pais_b = 200000
data = 2023 

while pais_a <= pais_b:
    pais_a = pais_a + (pais_a * 0.03)
    data += 1

print(f"O pais A vai passar o Pais b em {data}")
"""

pais_a = 80000
pais_b = 200000
data = 2023 

while pais_a <= pais_b:
    pais_a = pais_a + (pais_a * 0.03)
    pais_b = pais_b + (pais_b * 0.015) #No codigo acima eu coloquei como se fosse estagnar, porém como ela continua cresendo, por isso preciso colcoar esse aqui tbm.
    data += 1

print(f"O país A vai passar o país B em {data}")
print(f"O país A em {data} vai ter {pais_a:.2f}")
print(f"O país b em {data} vai ser {pais_b:.2f}")