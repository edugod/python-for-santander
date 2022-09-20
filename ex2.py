# Questão 2.
# Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
# dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
# esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”. Veja
# alguns exemplo abaixo:
# 💡 Entrada: 25.01 | Saída: (25,50]
# Entrada: 25.00 | Saída: [0,25]
# Entrada: 100.00 | Saída: (75,100]
# Entrada: -25.02 | Saída: Fora de intervalo

lista = [[0,25], [25,50], [50,75], [75,100]]
digitANumber = float(input("digite um número: ")) #float pq pode ser 0.03 não int
i = 0
whichInterval = 0
while i < len(lista):
    if digitANumber >= lista[i][0] and digitANumber <= lista[i][1]:
        whichInterval = lista[i]
    i+=1
if whichInterval != 0:
    print(whichInterval)
else:
    print('não está no intervalo')