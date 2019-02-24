"""
    Exercício Python #008 - Conversor de Medidas

    Escreva um programa que leia um valor em metros e o exiba
    convertido em centímetros e milímetros.
"""


def metro_para_quilometro(metros):
    return metros / 1000


def metro_para_hectometro(metros):
    return metros / 100


def metro_para_decametro(metros):
    return metros / 10


def metro_para_decimetro(metros):
    return metros * 10


def metro_para_centimetro(metros):
    return metros * 100


def metro_para_milimetro(metros):
    return metros * 1000


distancia = float(input("Uma distância em metros: "))
print(f'A medida de {distancia:.1f}m corresponte a:')
print(f'{metro_para_quilometro(distancia):9.4f}km')
print(f'{metro_para_hectometro(distancia):9.4f}hm')
print(f'{metro_para_decametro(distancia):9.4f}dam')
print(f'{metro_para_decimetro(distancia):9.4f}dm')
print(f'{metro_para_centimetro(distancia):9.4f}cm')
print(f'{metro_para_milimetro(distancia):9.4f}mm')
