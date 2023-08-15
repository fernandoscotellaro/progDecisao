'''
10)	Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo número informado é ou não um divisor do primeiro número informado.
'''

num1 = int(input("Insira aqui o primeiro número:"))
num2 = int(input("insira aqui o segundo número:"))

a = num2%num1

if ( a==0 ):
    print("O segundo número pode ser dividido pelo primeiro!")

else:
    print("O segundo número não pode ser divisível pelo primeiro!")
