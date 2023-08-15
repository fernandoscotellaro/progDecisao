'''
8)	Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10.
'''

num = int(input("Insira aqui um número inteiro:"))

answer = (f"{num} não está na faixa de 1 a 10", f"{num} está na faixa de 1 a 10")[num > 0 and num <= 10]

print(answer)