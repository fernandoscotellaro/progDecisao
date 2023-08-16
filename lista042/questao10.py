'''
10.	Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições devem seguir as regras da tabela abaixo:
Média:             Situação:
Abaixo de 3,0 =    Reprovado
Entre 3,0 e 6,9 =  Prova Final
A partir de 7,0 =  Aprovado
'''

nome = str(input("Insira aqui o seu nome:"))
nota1 = float(input("Insira aqui o valor da sua primeira nota:"))
nota2 = float(input("Insira aqui o valor da sua segunda nota:"))

cont = (nota1 + nota2) / 2

if (cont < 3.0):
    print(f"Sua média é {cont}, Você está reprovado!")

elif (cont > 3.0 and cont < 6.9):
    print(f"Sua média é {cont}, Você está em prova final!")

else:
    print(f"Sua média é {cont}, Você está aprovado!")