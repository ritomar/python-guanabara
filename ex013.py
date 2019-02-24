"""
    Exercício Python #013 - Reajuste Salarial

    Faça um algoritmo que leia o salário de um funcionário e mostre seu
    novo salário, com 15% de aumento.
"""


# Perceba que essa é a mesma função do Exercício #012
def porcentagem(valor, percentual):
    return valor * (percentual / 100)


salario = float(input("Qual é o salário do funcionário? R$ "))
percentual_aumento = 15  # Fixado o aumento em 15%, pode ler esse valor pelo teclado.
valor_aumento = porcentagem(salario, percentual_aumento)
novo_salario = salario + valor_aumento
print(
    f'Um funcionário que ganhava R$ {salario:.2f}, '
    f'com {percentual_aumento:.2f}% de aumento, passa a receber R$ {novo_salario:.2f}.'
)
