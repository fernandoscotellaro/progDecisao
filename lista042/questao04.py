'''
4.	Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso) correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o número inserido não corresponder à um dia da semana.
'''

nu = int(input("Insira aqui um número de 1 a 7:"))

if (nu == 1):
    print("O dia da semana é Domingo! :)")

elif (nu == 2):
    print("O dia da semana é Segunda-feira! :)")

elif (nu == 3):
    print("O dia da semana é Terça-feira! :)")

elif (nu == 4):
    print("O dia da semana é Quarta-feira! :)")

elif (nu == 5):
    print("O dia da semana é Quinta-feira! :)")

elif (nu == 6):
    print("O dia da semana é Sexta-feira! :)")

elif (nu == 7):
    print("O dia da Semana é sábado! :)")

else:
    print("O número inserido é inválido! :(")