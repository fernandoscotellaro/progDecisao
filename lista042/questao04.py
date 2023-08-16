'''
4.	Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso) correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o número inserido não corresponder à um dia da semana.
'''

num = int(input("Insira aqui um número de 1 a 7:"))

if (num == 1):
    print("O dia da semana é Domingo! :)")

elif (num == 2):
    print("O dia da semana é Segunda-feira! :)")

elif (num == 3):
    print("O dia da semana é Terça-feira! :)")

elif (num == 4):
    print("O dia da semana é Quarta-feira! :)")

elif (num == 5):
    print("O dia da semana é Quinta-feira! :)")

elif (num == 6):
    print("O dia da semana é Sexta-feira! :)")

elif (num == 7):
    print("O dia da Semana é sábado! :)")

else:
    print("O número inserido é inválido! :(")