'''
3)	Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou é ímpar.
'''

num = int(input("Insira aqui o número:"))

b= a%2

if (b==0):
    print("Seu número é par!")

elif (b==1):
    print("Seu número é impar!")