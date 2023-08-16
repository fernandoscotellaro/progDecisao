'''
2.	Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e 5000, ou acima de 5000.
'''

nu = float(input("Insira aqui o número:"))

if (nu < 1000):
    print("O número informado está abaixo de 1000!")

elif (nu > 1000 and nu < 5000):
    print("O número informado está entre 1000 e 5000!")

else:
    print("O número informado está acima de 5000!")