"""
    Exercício Python #006 - Dobro, Triplo e Raiz Quadrada

    Crie um algoritmo que leia um número e mostre seu dobro, triplo e
    raiz quadrada.
"""

n = int(input("Digite um número: "))
print(f'O dobro de {n} vale {n * 2}.')
print(f'O triplo de {n} vale {n * 3}.')
print(f'A raiz quadrada de {n} vale {n ** (1/2):.2f}.')
