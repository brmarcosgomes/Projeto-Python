"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.

"""  

nota1 = input("Nota numero 1: ")
nota2 = input("Nota numero 2: ")
int_nota1 = int(nota1)
int_nota2 = int(nota2)
media = (int_nota1 + int_nota2) / 2


if media == 10:
    print(f"Nota: {media} - Aprovado com distinção")

elif media >= 7:
    print(f"Nota: {media} - Aprovado")
    
elif media < 7:
    print(f"Nota: {media} - Reprovado")

else:
    print("Algo deu errado")
