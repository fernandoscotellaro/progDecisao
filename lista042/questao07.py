'''
7.	Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é o menor, ou ainda, se ambos são iguais
'''

num = int(input("Insira aqui o primeiro número:"))
num1 = int(input("Insira aqui o segundo número:"))

if (num1 > num):
    print("O segundo número é maior do que o primeiro!")

elif (num > num1):
    print("O primeiro número é maior do que o segundo!")

else:
    print("Os números são iguais!")