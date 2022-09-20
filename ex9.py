# Questão 9.
# Crie (manualmente ou sorteando os números) uma lista de 10 números e imprima:
# 1. uma lista com os 4 primeiros números;
# 2. uma lista com os 5 últimos números;
# 3. uma lista contendo apenas os elementos das posições pares;
# 4. uma lista contendo apenas os elementos das posições ímpares;

lista = [2, 4, 5, 7, 2, 4, 1, 3, 4, 8]
i = 0
while i <= 3:
    print (lista[i], 'na posição', i+1)
    i += 1
i = 4
while i < len(lista):
    print (lista[i], 'na posição', i+1)
    i +=1
i = 0
while i < len(lista):
    print(lista[i], 'item na posição par')
    i +=2
i = 1
while i < len(lista):
    print(lista[i], 'item na posição ímpar')
    i +=2
#------------------------------- método pythonzeira
lista = [5, 3, 9, 0, 1, 2, 6, 4, 7, 8]

print('Lista inicial:', lista, '\n')
print('Quatro primeiros elementos: ', lista[:4])
print('Cinco últimos elementos: ', lista[-5:])
print('Elementos nas posições pares: ', lista[::2])
print('Elementos nas posições ímpares: ', lista[1::2])
# muito mais fácil