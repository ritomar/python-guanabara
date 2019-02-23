"""
    Exercício Python #103 - Ficha do Jogador

    Faça um programa que tenha uma função chamada ficha(), que
    receba dois parâmetros opcionais: o nome de um jogador e
    quantos gols ele marcou. O programa deverá ser capaz de mostrar
    a ficha do jogador, mesmo que nenhum dado tenha sido
    informado corretamente.
"""


def ficha(nome='', gols=0):
    if not str(gols).isdigit():
        gols = 0
    if nome.strip() == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gol(s) no campeonado.'


n = input("Nome do Jogador: ")
g = input("Número de Gols: ")
print(ficha(n, g))
