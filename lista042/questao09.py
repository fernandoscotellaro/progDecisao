'''
9.	Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de idade, se é maior de idade, ou se é maior de 65 anos.
'''

idad = int(input("Insira aqui sua idade:"))

if (idad >= 18 and idad < 65):
    print("Você já está na maioridade!")

elif (idad <= 17 and idad > 0):
    print("Você ainda não etá na maioridade!")

else:
    if (idad >= 65):
        print("Você já está na terceira idade!")