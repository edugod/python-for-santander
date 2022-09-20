# Questão 4.
# Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
# a) o produto entre o dobro do primeiro e a metade do segundo.
# b) a soma entre o triplo do primeiro e o terceiro.
# c) o terceiro elevado ao cubo.

a = int(input('digite um numero inteiro: '))
b = int(input('digite um outro numero inteiro: '))
c = float(input('digite um numero real: '))

def programa (a,b,c):
    print((a*2) * (b/2))
    print((a*3) + c)
    print(c ** 3)

programa(a, b, c)