# Questão 1.
# Faça um programa que peça ao usuário um número e imprima todos os números de um até o
# número que o usuário informar.
# 💡 Exemplo:
# Se o usuário informar o número 5, seu programa deverá imprimir: 1 2 3 4 5.

digitANumber = input ("Digite um número: ")
i = 1
while i <= int(digitANumber):
        print(i)
        i += 1
        