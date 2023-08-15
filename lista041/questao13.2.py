'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem crescente.
'''

a = int(input("Insira aqui o primeiro número:"))
b = int(input("Insira aqui o segundo número:"))
c = int(input("Insira aqui o terceiro número:"))

# 1- a tem que ser menor que b
if ( a > b ):
    aux = a
    a = b
    b = aux

# 2- a tem que ser menor que c
if (a > c):
    aux = a
    a = c
    c = aux

# garantido até aqui que a é o menor dos 3
# agora é necessário garantir que b seja menor que c
if (b > c):
    aux = b
    b = c
    b = aux

# garantido até aqui que entre b e c, o b é menor, ou seja, o c é o maior de todos

print(f"Ordem crescente: {a}, {b} e {c}")