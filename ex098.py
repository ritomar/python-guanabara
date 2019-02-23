from time import sleep


def modulo(n):
    """
    Retorna o módulo de um número inteiro.
    :param n: Número para calcular o módulo.
    :return: O módulo do número.
    """
    return n if n >= 0 else -n


def contagem(inicio, fim, passo=1):
    print('-=' * 30)
    if passo == 0:
        print('Passo não pode ser zero.')
        return
    print(f'Contagem de {inicio} até {fim} de {modulo(passo)} em {modulo(passo)}')
    if inicio > fim and passo > 0: passo *= -1
    fim += (1 if passo > 0 else -1)

    for i in range(inicio, fim, passo):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')


contagem(1, 10, 0)
contagem(0, 0)
contagem(10, 0, 2)
contagem(12, -10, 7)
contagem(20, 0, -4)
