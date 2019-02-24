"""
    Exercício Python #007 - Média Aritmética

    Desenvolva um programa que leia as duas notas de um aluno,
    calcule e mostre a sua média.
"""


def media(a, b):
    return (a + b) / 2


nota_1 = float(input("Primeira nota do aluno: "))
nota_2 = float(input("Segunda nota do aluno: "))
print(f'A média entre {nota_1:.1f} e {nota_2:.1f} é igual a {media(nota_1, nota_2):.1f}')
