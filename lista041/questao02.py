'''
2)	Desenvolver um programa que permita ao aluno responder qual a capital do Brasil. O programa deverá exibir se a resposta está certa ou errada.
'''

nome = str(input("Insira aqui qual a capital do Brasil:"))
capital = ("Brasília")

if (nome == capital):
    print("Parabéns, você acertou!")

else:
    print(f"Ah, que pena! Você errou :(")