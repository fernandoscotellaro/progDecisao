'''
Crie um programa que pergunte a idade do usuário e em seguida informe se este usuário é menor de idade ou maior de idade.
'''

old = int(input("Informe a sua idade:"))

answer = (f"Você tem {old} anos, você ainda é menor de idade!", f"Você já tem {old} anos, você é maior de idade!")[old>=18]

print(answer)