"""
    Exercício Python #020 - Sorteando uma ordem na lista

    O mesmo professor do desafio anterior que sortear uma ordem de
    apresentação dos trabalhos dos alunos. Faça um programa que leia
    os nomes dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle

# Faz a leitura dos nomes
n1 = input("Nome do aluno 1: ")
n2 = input("Nome do aluno 2: ")
n3 = input("Nome do aluno 3: ")
n4 = input("Nome do aluno 4: ")

alunos = [n1, n2, n3, n4]
shuffle(alunos)
print("A ordem de apresentação será:", alunos)
