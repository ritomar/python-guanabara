"""
    Exercício Python #004 - Dissecando uma Variável

    Faça um programa que leia algo pelo teclado e mostre na tela o seu
    tipo primitivo e todas as informações possíveis sobre ele.
"""


entrada = input("Digite algo: ")
print(f"O tipo primitivo desse valor é {type(entrada)}")
print("Só tem espaços?", entrada.isspace())
print("É um número?", entrada.isnumeric())
print("É alfabético?", entrada.isalpha())
print("É alfanumérico?", entrada.isalnum())
print("Está em maiúsculas?", entrada.isupper())
print("Está em minúsculas?", entrada.islower())
print("Está capitalizada?", entrada.istitle())
print("É indentificador?", entrada.isidentifier())
print("É imprimível?", entrada.isprintable())

