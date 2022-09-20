# Questão 5.
# Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o
# assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser
# sim ou não:
# 1. Mora perto da vítima?
# 2. Já trabalhou com a vítima?
# 3. Telefonou para a vítima?
# 4. Esteve no local do crime?
# 5. Devia para a vítima?
# Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5
# pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
# necessitando de outras investigações. Valores abaixo de 2 são liberados.
# No seu programa, você deve fazer essas perguntas e, de acordo com as respostas do usuário,
# você vai informar como a polícia o considera.

contador = int(0)
questionOne = input('mora perto da vítima? ')
questionTwo = input('Já trabalhou com a vítima? ')
questionThree = input('Telefonou para a vítima? ')
questionFour = input('Esteve no local do crime? ')
questionFive = input('Devia para a vítima ')

if questionOne == str('sim'):
    contador += 1
if questionTwo == str('sim'):
    contador += 1
if questionThree == str('sim'):
    contador += 1
if questionFour == str('sim'):
    contador += 1
if questionFive == str('sim'):
    contador += 1

if contador == 5:
    print('é assasino')
if contador == 3 or contador == 4:
    print('é cúmplice')
if contador == 2:
    print('suspeito')
if contador < 2:
    print('liberado')

print(contador)