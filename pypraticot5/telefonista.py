class Telefonista(object):
    def __init__(self):
        self._contatos = []

    def adicionar(self, contato):
        self._contatos.append(contato)
