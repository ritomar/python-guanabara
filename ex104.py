"""
    Exercício Python #104 - Validadando entrada de dados em Python

    Faça um programa que tenha uma função chamada ficha(), que
    receba dois parâmetros opcionais: o nome de um jogador e
    quantos gols ele marcou. O programa deverá ser capaz de mostrar
    a ficha do jogador, mesmo que nenhum dado tenha sido
    informado corretamente.
"""
from util import print_red


def input_int(msg=''):
    while True:
        valor_lido = input(msg)
        if valor_lido.isdigit():
            return int(valor_lido)
        else:
            print_red('Erro! Digite um número inteiro válido.', flush=True)


n = input_int("Digite um número: ")
print(f'Você digitou {n}.')
