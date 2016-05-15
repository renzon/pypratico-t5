import unittest

from pypraticot5 import telefonista


class TelefonistasTests(unittest.TestCase):
    def test_instanciacao_telefonista(self):
        telefonista_obj = telefonista.Telefonista()
        self.assertListEqual([], telefonista_obj._contatos)

    def test_adicionar_um_contato(self):
        contato = ('Renzo', '2345678')
        telefonista_obj = telefonista.Telefonista()
        telefonista_obj.adicionar(contato)
        self.assertListEqual([contato], telefonista_obj._contatos)
    def test_adicionar_dois_contato(self):
        renzo = ('Renzo', '2345678')
        karen = ('Karen', '8765432')
        telefonista_obj = telefonista.Telefonista()
        telefonista_obj.adicionar(renzo)
        telefonista_obj.adicionar(karen)
        self.assertListEqual([renzo, karen], telefonista_obj._contatos)

    def test_ligar_para_um_contato(self):
        contato = ('Renzo', '2345678')
        telefonista_obj = telefonista.Telefonista()
        telefonista_obj.adicionar(contato)
        ligacoes=telefonista_obj.ligar()
        self.assertListEqual(['Telefonando de verdade para 2345678. Olá Renzo'],
                             ligacoes)
