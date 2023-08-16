'''
9.	Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de idade, se é maior de idade, ou se é maior de 65 anos.
'''

idade = int(input("Insira aqui sua idade:"))

if (idade >= 18 and idade < 65):
    print("Você já está na maioridade!")

elif (idade <= 17 and idade > 0):
    print("Você ainda não etá na maioridade!")

else:
    if (idade >= 65):
        print("Você já está na terceira idade!")