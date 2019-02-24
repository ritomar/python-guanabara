"""
    Exercício Python #012 - Calculando Descontos

    Faça um algoritmo que leia o preço de um produto e mostre seu
    novo preço, com 5% de desconto.
"""


def desconto(valor, percentual):
    return valor * (percentual / 100)


preco = float(input("Qual é o preço do produto? R$ "))
percentual_desc = 5  # Fixado o desconto em 5%, pode ler esse valor pelo teclado.
valor_desc = desconto(preco, percentual_desc)
novo_preco = preco - valor_desc
print(
    f'O produto que custava R$ {preco:.2f}, na promoção '
    f'com desconto de {percentual_desc:.2f}% vai custar R$ {novo_preco:.2f}.'
)
