'''
4)	Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por 4 e 5”.
'''

num = int(input("insira aqui um número:"))

b = num%4
c = num%5
if (b==0 and c==0):
    print("A divisão desse número pode ser realizada por 4 e por 5!")

else:
    print("O valor não é divisível por 4 e nem por 5")