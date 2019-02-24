"""
    Exercício Python #016 - Quebrando um número

    Crie um programa que leia um número Real qualquer pelo teclado e
    mostre na tela a sua porção inteira.

    Ex: Digite um número: 6.127
        O número 6.127 tem a parte inteira 6.
"""

from math import trunc


def truncar(n):
    # Função truncar personalizada.
    return int(n)


num = float(input("Digite um valor: "))
print("Com a função trunc() a biblioteca math():")
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}.')
print()
print("Com a função truncar() que criamos de forma personalizada:")
print(f'O valor digitado foi {num} e a sua porção inteira é {truncar(num)}.')
