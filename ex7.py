# Questão 7.
# Faça um programa que leia as coordenadas de 2 (dois) pontos em um plano cartesiano 2D: a
# coordenada x do primeiro ponto (x_1), a coordenada y do primeiro ponto (y_1), a coordenada x do
# segundo ponto (x_2) e a coordenada y do segundo ponto (y_2). Em seguida, calcule a distância
# euclidiana entre os pontos, utilizando a equação abaixo:
# 𝑑 = (𝑥2 − 𝑥1)² + (𝑦2 − 𝑦1)²

from math import sqrt

firstPointX = float(input('primeiro ponto x: '))
firstPointY = float(input('primeiro ponto y: '))
secondPointX = float(input('segundo ponto x: '))
secondPointY = float(input('segundo ponto y: '))

def euclidianDistance(x1,y1,x2,y2):
    return sqrt(((x2 - x1)** 2) + ((y2 - y1)** 2))

print(euclidianDistance(firstPointX, firstPointY, secondPointX, secondPointY))
