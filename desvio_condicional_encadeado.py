'''
Crie um programa que pergunte um número ao usuário. Em seguida o programa deve informar se o número inserido está abaixo de 100, entre 100 e 200 ou acima de 200.
'''

num = int(input("Insira aqui o número:"))

if (num < 100):
    print("Seu número é inferior a 100")

else:
    if (num <= 200):
        print("Seu número está entre 100 e 200")

    else:
            print("Seu número é superior a 200")

