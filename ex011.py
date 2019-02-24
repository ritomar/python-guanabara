"""
    Exercício Python #011 - Pintando Parede

    Faça um programa que leia a largura e a altura de uma parede em
    metros, calcule sua área e a quantidade de tinta necessária para
    pintá-la, sabendo que cada litro de tinta, pinta uma área 2m².
"""


def area(largura, altura):
    return largura * altura


def quantidade_tinta(largura, altura):
    # Calcula a quantidade de litros de tinta necessários para pintar,
    # calculando a área da parede em m² e dividindo pelo rendimento
    # de cada litro de tinta (neste exercício, 2m² por litro).
    return area(largura, altura) / 2


larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))

print(f'Sua parede tem a dimensão de {larg} x {alt} e sua área é de {area(larg, alt):.3f}')
print(f'Para pintar essa parede, você precisará de {quantidade_tinta(larg, alt):.4f}l de tinta')
