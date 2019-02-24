"""
    Exercício Python #023 - Separando dígitos de um número

    Faça um programa que leia um número de 0 a 9999 e mostre na tela
    cada um dos seus dígitos separados.
    Ex:
        Digite um número: 1834
        unidade: 4, dezena: 3, centena: 8, milhar 1.
"""

n_lido = int(input("Digite um número: "))
n = n_lido  # Mantem o número lido para exibir no final

unidade = n % 10  # Salva a unidade
n //= 10  # Remove a unidade
dezena = n % 10  # Salva a dezena
n //= 10  # Remove a dezena
centena = n % 10  # Salva a centena
n //= 10  # Remove a centena
milhar = n % 10  # Salva a milhar
n //= 10  # Remove a milhar. O número será reduzido a zero.

print(f"Analisando o número {n_lido}...")
print(f"unidade: {unidade}, dezena: {dezena}, centena: {centena}, milhar {milhar}.")
