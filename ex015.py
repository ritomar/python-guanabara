"""
    Exercício Python #015 - Aluguel de Carros

    Escreva um programa que pergunte a quantidade de Km
    percorridos por um carro alugado e a quantidade de dias pelos
    quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
    custa R$ 60 por dia e R$ 0,15 por Km rodado.
"""


def preco_pelos_dias(qtd_dias):
    # Fixado em R$ 60 por dia
    return qtd_dias * 60


def preco_pelos_km_rodados(qtd_km):
    # Fixado em R$ 0,15 por Km rodado
    return qtd_km * 0.15


dias = int(input("Quantidade de dias alugados: "))
km = float(input("Quantos Km foram percorridos: "))
total = preco_pelos_dias(dias) + preco_pelos_km_rodados(km)
print(f'O total a pagar pelo aluguel é de R$ {total:.2f}.')
