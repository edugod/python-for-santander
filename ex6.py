# Questão 6.
# Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.
lista_exemplo = [2, 3, 4, 2.5]

def soma_da_lista(lista):
    return sum(lista)

resultado = soma_da_lista(lista_exemplo)

print("A soma dos items da lista =", resultado)