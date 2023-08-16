'''
6.	Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela: “Dados inseridos estão incorretos”.
'''

nas = int(input("Insira aqui o ano que você nasceu:"))
ano = int(input("Insira aqui o ano que você está:"))

conta = (ano - nas)

if (ano > nas):
    print(f"Você tem {conta} anos!")

else:
    print("Dados inseridos incorretamente!")