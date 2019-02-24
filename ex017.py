"""
    Exercício Python #017 - Catetos e Hipotenusa

    Crie um programa que leia o comprimento do cateto oposto e
    do cateto adjacente de um triânguo retângulo, calcule e
    mostre o comprimento da hipotenusa.
"""

from math import hypot


def hipotenusa(cateto_oposto, cateto_adjacente):
    # Função hipotenusa personalizada.
    return ((cateto_adjacente ** 2) + (cateto_oposto ** 2)) ** (1 / 2)


co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

print("Com a função hypot() a biblioteca math:")
print(f'A hipotenusa vai medir {hypot(co, ca):.2f}.')
print()
print("Com a função hipotenusa() que criamos de forma personalizada:")
print(f'A hipotenusa vai medir {hipotenusa(co, ca):.2f}.')
