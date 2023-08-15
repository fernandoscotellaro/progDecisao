'''
6)	Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o maior valor e o menor valor lido
'''

a = int(input("Insira aqui o primeiro valor:"))
b = int(input("insira aqui mais um valor:"))

if (a > b):
    print(f"O primeiro número é maior que o segundo! a diferença entre eles é {a - b}")

elif (b > a):
    print(f"O segundo número é maior que o primeiro! a diferença entre eles é {b - a}")