"""
    Exercício Python #024 - Verificando as primeiras letras de um texto

    Crie um programa que leia o nome de uma cidade e diga se ela
    começa ou não com o nome "SANTO".
"""


def inicia_com(texto, inicio):
    texto.strip()
    inicio.strip()
    return str(texto[:len(inicio)]).upper() == str(inicio).upper()


s = input("Digite o nome de uma cidade: ")
print(inicia_com(s, 'santo'))
