'''
11)	Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado somente o algarismo das centenas.
'''

a = int(input("insira aqui um número inteiro de 3 algarismos:"))

b = int (a / 100)

if (a >= 100):
    print(f"A casa de centena desse número é: {b}")
