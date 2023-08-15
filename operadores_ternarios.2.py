'''
Crie um programa que pergunte a idade do usuário e em seguida informe se este usuário é menor de idade ou maior de idade.
'''

old = int(input("Informe a sua idade:"))

answer = "Você é maior de idade!" if old >= 18 else "Você é menor de idade!"

print(answer)