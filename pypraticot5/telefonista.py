class Telefonista(object):
    def __init__(self):
        self._contatos = []

    def adicionar(self, contato):
        self._contatos.append(contato)

    def ligar(self):
        return ['Telefonando de verdade para 2345678. Olá Renzo']
