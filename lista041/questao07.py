'''
7)	Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo deste valor, ou seja, o número lido como sendo positivo.
'''

numero = int(input("Insira aqui um valor inteiro positivo ou negativo:"))

if (numero < 0):
    print(f"O módulo desse número é: {numero * -1}")