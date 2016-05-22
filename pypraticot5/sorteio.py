class SorteioExcecao(Exception):
    pass


def sortear(lista):
    if len(lista)==0:
        raise  Exception('Não é possível sortear elemento de lista vazia')
    return lista[0]
