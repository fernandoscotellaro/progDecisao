'''
5)	Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor da média obtida pelo aluno.
'''

a = float(input("Insira aqui a sua primeira nota:"))
b = float(input("Insira aqui a sua segunda nota:"))
c = float(input("Insira aqui a sua terceira nota:"))
d = float(input("Insira aqui a sua quarta nota:"))

media = (a + b + c +d) / 4

if (media >= 5):
    print(f"A sua média é suficiente ({media}). Você foi aprovado!")

else:
    print(f"Sua média não foi suficiente ({media}). Você não foi aprovado!")
