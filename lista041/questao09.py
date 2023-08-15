'''
9)	Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou nulo.
'''

num = int(input("Insira aqui um número qualquer:"))

if (num < 0):
    print(f"O número {num} é negativo!")

elif (num > 0):
    print(f"O número {num} é positivo!")

else:
    print(f"O número {num} é nulo!")