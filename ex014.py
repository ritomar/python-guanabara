"""
    Exercício Python #014 - Conversor de Temperaturas

    Escreva um programa que converta uma temperatura
    digitada em ˚C e converta para ˚F.
"""


def celsius_para_fahrenheit(temperatura_celsius):
    return ((9 * temperatura_celsius) / 5) + 32


c = float(input("Informe a temperatura em ˚C: "))
f = celsius_para_fahrenheit(c)
print(f'A temperatura de {c:.1f}˚C corresponde a {f:.1f}˚F!')
