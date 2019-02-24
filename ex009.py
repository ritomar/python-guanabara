"""
    Exercício Python #009 - Tabuada

    Faça um programa que leia um número inteiro qualquer e mostre na
    tela a sua tabuada.
"""


def tabuada(n):
    s = '    '
    print()
    print(f'{"Soma":12}',
          f'{"Sub":12}',
          f'{"Mult":13}',
          f'{"Div":15}', sep=s)
    print('-' * 12, '-' * 12, '-' * 13, '-' * 15, sep=s)

    print(f'{n:2d} + {1:2d} = {n + 1:2d}',
          f'{n:2d} - {1:2d} = {n - 1:2d}',
          f'{n:2d} x {1:2d} = {n * 1:3d}',
          f'{n:2d} \xF7 {1:2d} = {n / 1:5.2f}', sep=s)
    print(f'{n:2d} + {2:2d} = {n + 2:2d}',
          f'{n:2d} - {2:2d} = {n - 2:2d}',
          f'{n:2d} x {2:2d} = {n * 2:3d}',
          f'{n:2d} \xF7 {2:2d} = {n / 2:5.2f}', sep=s)
    print(f'{n:2d} + {3:2d} = {n + 3:2d}',
          f'{n:2d} - {3:2d} = {n - 3:2d}',
          f'{n:2d} x {3:2d} = {n * 3:3d}',
          f'{n:2d} \xF7 {3:2d} = {n / 3:5.2f}', sep=s)
    print(f'{n:2d} + {4:2d} = {n + 4:2d}',
          f'{n:2d} - {4:2d} = {n - 4:2d}',
          f'{n:2d} x {4:2d} = {n * 4:3d}',
          f'{n:2d} \xF7 {4:2d} = {n / 4:5.2f}', sep=s)
    print(f'{n:2d} + {5:2d} = {n + 5:2d}',
          f'{n:2d} - {5:2d} = {n - 5:2d}',
          f'{n:2d} x {5:2d} = {n * 5:3d}',
          f'{n:2d} \xF7 {5:2d} = {n / 5:5.2f}', sep=s)
    print(f'{n:2d} + {6:2d} = {n + 6:2d}',
          f'{n:2d} - {6:2d} = {n - 6:2d}',
          f'{n:2d} x {6:2d} = {n * 6:3d}',
          f'{n:2d} \xF7 {6:2d} = {n / 6:5.2f}', sep=s)
    print(f'{n:2d} + {7:2d} = {n + 7:2d}',
          f'{n:2d} - {7:2d} = {n - 7:2d}',
          f'{n:2d} x {7:2d} = {n * 7:3d}',
          f'{n:2d} \xF7 {7:2d} = {n / 7:5.2f}', sep=s)
    print(f'{n:2d} + {8:2d} = {n + 8:2d}',
          f'{n:2d} - {8:2d} = {n - 8:2d}',
          f'{n:2d} x {8:2d} = {n * 8:3d}',
          f'{n:2d} \xF7 {8:2d} = {n / 8:5.2f}', sep=s)
    print(f'{n:2d} + {9:2d} = {n + 9:2d}',
          f'{n:2d} - {9:2d} = {n - 9:2d}',
          f'{n:2d} x {9:2d} = {n * 9:3d}',
          f'{n:2d} \xF7 {9:2d} = {n / 9:5.2f}', sep=s)
    print(f'{n:2d} + {10:2d} = {n + 10:2d}',
          f'{n:2d} - {10:2d} = {n - 10:2d}',
          f'{n:2d} x {10:2d} = {n * 10:3d}',
          f'{n:2d} \xF7 {10:2d} = {n / 10:5.2f}', sep=s)

    print('-' * 12, '-' * 12, '-' * 13, '-' * 15, sep=s)


# Remova os comentários abaixo para ver todas as tabuadas.
# tabuada(1)
# tabuada(2)
# tabuada(3)
# tabuada(4)
# tabuada(5)
# tabuada(6)
# tabuada(7)
# tabuada(8)
# tabuada(9)
# tabuada(10)

n = int(input("Digite um número para ver sua tatuada: "))
tabuada(n)
