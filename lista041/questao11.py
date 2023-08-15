'''
11)	Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado somente o algarismo das centenas.
'''

a = int(input("insira aqui um número inteiro de 3 algarismos:"))



if (a >= 100 and num <= 999):
    b = int(a / 100)
    print(f"O algarismo da casa de centena desse número é: {b}!")

else:
    print(f"O valor informado não possui algarismos suficientes!")
