"""
    Exercício Python #022 - Analisador de Textos

    Crie um programa que leia o nome completo de uma pessoa e
    mostre:
    > O nome com todas letras maiúsculas e minúsculas.
    > Quantas letras o nome tem (sem contar espaços)
    > Quantas letras tem o primeiro nome
"""

nome = input("Digite o seu nome completo: ").strip()
print("Analisando o seu nome...")
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome ao todo {len(nome) - nome.count(" ")} letras')
primeiro_nome = nome.split()[0]

# Outra forma de fazer a mesma coisa sem listas
# primeiro_nome = nome[:nome.find(" ")]

print(f'Seu primeio nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras')
