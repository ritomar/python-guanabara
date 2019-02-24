"""
    Exercício Python #019 - Sorteando um item na lista

    Um professor quer sortear um dos seus quatro alunos para apagar
    o quadro. Faça um programa que ajude ele, lendo o nome deles e
    escrevendo o nome escolhido.
"""

from random import randint

# Solução mais sofisticada que não usa listas (assunto não visto).
# Baseia-se na utilização do método find() de strings

# Faz a leitura dos nomes
n1 = input("Nome do aluno 1: ")
n2 = input("Nome do aluno 2: ")
n3 = input("Nome do aluno 3: ")
n4 = input("Nome do aluno 4: ")

# n1 = 'Ana'
# n2 = 'Bia'
# n3 = 'Carla'
# n4 = 'Dani'

print(f'Nomes: {n1}, {n2}, {n3}, {n4}.')

# Coloca todos os nomes em uma sequencia de busca ("nomes")
# delimitados por um números.
# Por exemplo, se os nomes lidos forem Ana, Bia, Carla, Dani
# a sequencia de busca será: 1Ana2Bia3Carla4Dani5
nomes = '1' + n1 + '2' + n2 + '3' + n3 + '4' + n4 + '5'
print("Sequencia de busca:", nomes)

# Escolhe um número entre 1 e quatro
escolhido = randint(1, 4)
print('Escolhido: ', escolhido)

# Acha o início do nome escolhido na sequencia de busca.
# O início será a posição do número escolhido + 1
# Para 1Ana2Bia3Carla4Dani5 se o número escolhido for 4
# o início será a posição 15 da sequencia de busca
inicio = nomes.find(str(escolhido)) + 1
print('Posição inicial da sequencia de busca:', inicio)

# O fim do nome escolhido na sequencia de busca
# será a posição "número escolhido + 1"
fim = nomes.find(str(escolhido + 1))
print('Posição final da sequencia de busca:', fim)

# Mostra o nome escolhido, a partir da sequencia de busca "nomes"
print('Aluno Escolhido:', nomes[inicio:fim])
