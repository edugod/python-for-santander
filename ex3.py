# Questão 3.
# Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
# área desse círculo. Lembrando que a área de círculo é dada pela equação: A = ℼ r^2.
# 💡 Dica: Para utilizar um valor mais preciso do pi (ℼ), você pode importar a biblioteca math, e
# utilizar o math.pi, como ilustrado no código abaixo:
from math import pi

def calcular_area_circulo():
    raio = int(input('digite um raio: '))
    area = pi * raio ** 2
    print(round(area, 2))

calcular_area_circulo()