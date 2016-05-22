from pypraticot5.telefone import Telefone


class Telefonista(object):
    def __init__(self):
        self._telefone = Telefone()
        self._contatos = []

    def adicionar(self, contato):
        self._contatos.append(contato)

    def ligar(self):
        for nome, numero_telefone in self._contatos:
            msg = self._telefone.telefonar(numero_telefone)
            yield '{msg}. Olá {nome}'.format(msg=msg, nome=nome)
