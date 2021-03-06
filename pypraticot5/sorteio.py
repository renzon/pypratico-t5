from random import choice


class SorteioExcecao(Exception):
    pass


def sortear(lista):
    if len(lista) == 0:
        raise SorteioExcecao('Não é possível sortear elemento de lista vazia')
    return choice(lista)
