'''
2.	Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e 5000, ou acima de 5000.
'''

num = float(input("Insira aqui o número:"))

if (num < 1000):
    print("O número informado está abaixo de 1000!")

elif (num > 1000 and num < 5000):
    print("O número informado está entre 1000 e 5000!")

else:
    print("O número informado está acima de 5000!")