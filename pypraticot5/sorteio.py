from random import shuffle


class SorteioExcecao(Exception):
    pass


def sortear(lista):
    if len(lista) == 0:
        raise SorteioExcecao('Não é possível sortear elemento de lista vazia')
    lista = list(lista)
    shuffle(lista)
    return lista[0]
