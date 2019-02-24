"""
    Exercício Python #010 - Conversor de Moedas

    Crie um programa que leia quanto dinheiro uma pessoa tem na
    carteira e mostre quantos dólares ela pode comprar.
"""


def cotacao_dolar():
    # Um desafio é melhorar essa função para buscar a cotação
    # automaticamente na Internet e retornar atualizada.
    return 3.27


def real_para_dolar(valor_em_reais):
    cotacao = cotacao_dolar()
    return valor_em_reais / cotacao


valor = float(input("Quanto Dinheiro você tem na carteira? R$ "))
print(f'Com R${valor:.2f} você pode comprar US${real_para_dolar(valor):.2f}')
