'''
1)	Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a metade deste número, senão, ele deverá exibir o número sem alterações.
'''

num = float(input("Insira aqui o número:"))
conta = num / 2
if (num > 20):
    print(F"A metade desse número é: {conta}")

else:
    print(f"Não foi possível realizar a operação :(, seu número é: {num} ")