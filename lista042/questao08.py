'''
8.	Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável o maior destes 3 números inseridos. O valor da variável maior deverá ser exibido ao final.
'''

numum = int(input("Insira um número:"))
num2 = int(input("Insira outro número:"))
num3 = int(input("Insira mais um número:"))

maior = numum

if (numum < num2):
    maior = num2

if (numum < num3):
    maior = num3

print(f"O maior número é {maior}")

