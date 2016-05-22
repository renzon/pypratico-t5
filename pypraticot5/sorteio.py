from random import randint


class SorteioExcecao(Exception):
    pass


def sortear(lista):
    if len(lista) == 0:
        raise SorteioExcecao('Não é possível sortear elemento de lista vazia')
    indice = randint(0, len(lista)-1)
    print(indice)
    return lista[indice]
