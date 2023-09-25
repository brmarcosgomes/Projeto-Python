"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
from datetime import time

hora = input("Escreva somente a hora ([00]:00:00): ")
minutos = input("Escreva os minutos (00:[00]:00): ")
segundos = input("Escreva os segundos(00:00:[00]): ")

     
try:
    hora_exata = time(hour=int(hora), minute=int(minutos), second=int(segundos))
    if hora_exata > time(hour=00, minute=00,second=00) and hora_exata < time(hour=11, minute=59,second=59):
        print("Bom dia!")
    elif hora_exata > time(hour=12, minute=00,second=00) and hora_exata < time(hour=18, minute=59,second=59):
        print("Boa Tarde!")
    elif hora_exata > time(hour=19, minute=00,second=00) and hora_exata < time(hour=23, minute=59,second=59):
        print("Boa noite!")
    else:
        ...
except:
    print("Valor invalido!")

