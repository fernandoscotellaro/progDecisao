'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem crescente.
'''

a = float(input("Insira aqui o primeiro número:"))
b = float(input("Insira aqui o segundo número:"))
c = float(input("Insira aqui o terceiro número:"))

if a <= b and a <= c and b <= c:
    print(f'A ordem crescente é {a} , {b} e {c}')
elif a <= b and a <=c and c <= b:
    print(f'A ordem crescente é {a} , {c} e {b}')
elif b <= a and b <= c and a <= c:
    print(f'A ordem crescente é {b} , {a} e {c}')
elif b <= a and b <= c and c <= a:
    print(f'A ordem crescente é {b} , {c} e {a}')
elif c <= a and c <= b and a <=b:
    print(f'A ordem crescente é {c} , {a} e {b}')
elif c <= a and c <= b and b <= a:
    print(f'A ordem crescente é {c} , {b} e {a}')