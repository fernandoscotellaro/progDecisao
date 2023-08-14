'''
Crie um programa que pergunte dois números ao usuário. Em seguida o programa deverá somar os dois números e apresentar o resultado se o valor for maior que 10.
'''

num1 = int(input("Insira aqui o primeiro valor :"))
num2 = int(input("Insira aqui o segundo valor :"))

conta = num1 + num2

if (conta > 10):
    print(f"A soma dos dois valores:{conta}")

elif (conta < 10):
    print("Impossível responder!")

print("FIM DO PROGRAMA")

