"""
    Exercício Python #018 - Seno, Cosseno e Tangente

    Faça um programa que leia um ângulo qualquer e mostre na tela
    o valor do seno, cosseno e tangente desse ângulo.
"""

from math import sin, cos, tan, radians


def seno(angulo_em_graus):
    # Função personalizada que recebe a medida em graus.
    return sin(radians(angulo_em_graus))


def cosseno(angulo_em_graus):
    # Função personalizada que recebe a medida em graus.
    return cos(radians(angulo_em_graus))


def tangente(anangulo_em_graus):
    # Função personalizada que recebe a medida em graus.
    return tan(radians(anangulo_em_graus))


angulo = float(input("Digite o ângulo que você deseja: "))
s = seno(angulo)
c = cosseno(angulo)
t = tangente(angulo)

print(f'O ângulo de {angulo}˚ tem o SENO de {s:.2f}')
print(f'O ângulo de {angulo}˚ tem o COSSENO de {c:.2f}')
print(f'O ângulo de {angulo}˚ tem a TANGENTE de {t:.2f}')
