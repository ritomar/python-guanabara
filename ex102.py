"""
    Exercício Python #102 - Função para Fatorial

    Crie um programa que tenha uma função fatorial() que receba dois
    parâmetros: o primeiro que indique o número a calcular e o outro
    chamado show, que será um valor lógico (opcional) indicando se
    será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(n, show=False):
    """
    Calcula o fatorial e um número.
    :param n: O número a ser usado no cálculo.
    :param show: (opcinal) Mostrar a conta. Padrão: Falso
    :return: O valor do Fatorial de um número n.
    """
    fatorial_ = 1
    for k in range(n, 0, -1):
        fatorial_ *= k
        if show:
            print(f'{k} = ' if k == 1 else f'{k} x ', end='')

    return fatorial_


help(fatorial)
print(fatorial(5))
print(fatorial(5, True))
