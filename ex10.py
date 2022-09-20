# Na música, uma nota tem um tom (sua frequência, resultando em quão grave ou agudo é o
# som) e uma duração (por quanto tempo a nota soa). Neste problema, estamos interessados
# apenas na duração das notas.
# Marcos está dando os primeiros passos para ser um compositor de jingles. Ele está tendo alguns
# problemas, mas ao menos ele está criando melodias agradáveis e ritmos atrativos. Um jingle é
# dividido em uma sequência de compassos, e um compasso é formado de uma série de notas.
# A duração de uma nota é indicada pela sua forma. Neste problema, iremos utilizar letras
# maiúsculas para indicar a duração de uma nota. A seguinte tabela lista todas as notas
# disponíveis:
# W=1; H=1/2; Q=1/4; E=1/8; S=1/16; T=1/32; X=1/64 <> ID / DURAÇÃO

# A duração de um compasso é a soma da duração de suas notas. Nos jingles de Marcos, cada
# compasso tem a mesma duração. Como Marcos é apenas um iniciante, seu famoso professor
# Johann Sebastian III o ensinou que a duração de um compasso deve ser sempre 1.
# Por exemplo, Marcos escreveu uma composição contendo cinco compassos, dentre os quais
# quatro possuem a duração correta e um está errado. No exemplo abaixo, cada compasso é
# delimitado com barras e cada nota é representada como na tabela acima.
# Marcos gosta de computadores assim como de música. Ele quer que você escreva um programa
# que determine, para cada uma de suas composições, quantos compassos possuem a duração
# correta e quais são os compassos com duração incorreta.
# Exemplo de Entrada Exemplo de Saída
# /HH/QQQQ/XXXTXTEQH/W/HW/ Qtd. de Corretos: 4
# Incorretos: HW
# /W/W/SQHES/ Qtd. de Corretos: 3
# /WE/TEX/THES/ Qtd. de Corretos: 0
# Incorretos: [WE, TEX, THES]

# Um jingle é dividido em uma sequência de compassos, e um compasso é formado de uma série de notas.
# CADA COMPASSO TEM Q SER = 1

duracao_da_nota = {
  'W': 1,
  'H': 1/2,
  'Q': 1/4,
  'E': 1/8,
  'S': 1/16,
  'T': 1/32,
  'X': 1/64
}

composicao = '/HH/QQQQ/XXXTXTEQH/W/HW/'

# O método .strip() elimina o caracter que você colocar entre os parênteses, caso ele esteja no início ou no final da string
# O método .split() divide a string no caractere especificado entre os parênteses, gerando uma lista como resultado
compassos = composicao.strip('/').split('/')

print(compassos)

qtd_corretos = 0
incorretos = []

for compasso in compassos:
  duracao_compasso = 0
  for nota in compasso:
    duracao_compasso += duracao_da_nota[nota]
  
  if duracao_compasso == 1:
    qtd_corretos += 1
  else:
    incorretos.append(compasso)

print('Qtd. de Corretos:', qtd_corretos)
if len(incorretos) > 0:
  print('Incorretos:', incorretos)