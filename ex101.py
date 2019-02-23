"""
    Exercício Python #101 - Funções para votação

    Crie um programa que tenha uma função chamada voto() que vai
    receber como parâmetro o ano de nascimento de uma pessoa,
    retornando um valor literal indicando se uma pessoa tem voto
    NEGADO, OPCIONAL, ou OBRIGATÓRIO nas eleições.
"""
from datetime import datetime


def voto(ano_de_nascimento):
    ano_atual = datetime.now().year
    if (ano_de_nascimento <= 0) and (ano_de_nascimento <= 99):
        ano_de_nascimento = ano_de_nascimento + ((ano_atual // 100) * 100)
        if ano_de_nascimento > ano_atual:
            ano_de_nascimento -= 100
    idade = ano_atual - ano_de_nascimento
    if (idade < 0) or (idade > 120):
        return f'Idade inválida! Não pode ter nascido em {ano_de_nascimento}'
    elif (idade >= 0) and (idade < 16):
        return f'Não vota! Nasceu em {ano_de_nascimento} e a idade é {idade}.'
    elif (idade >= 18) and (idade < 65):
        return f'Voto obrigatório! Nasceu em {ano_de_nascimento} e a idade é {idade}.'
    else:
        return f'Voto opcional! Nasceu em {ano_de_nascimento} e a idade é {idade}.'


print(voto(datetime.now().year - 121))
print(voto(datetime.now().year - 120))
print(voto(datetime.now().year - 65))
print(voto(datetime.now().year - 64))
print(voto(datetime.now().year - 18))
print(voto(datetime.now().year - 17))
print(voto(datetime.now().year - 16))
print(voto(datetime.now().year - 15))
print(voto(datetime.now().year - 0))
print(voto(datetime.now().year + 1))

print()

print(voto(99))
print(voto(54))
print(voto(55))
print(voto(1))
print(voto(2))
print(voto(3))
print(voto(4))
print(voto(19))
print(voto(20))
print(voto(21))
