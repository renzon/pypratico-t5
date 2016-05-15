import unittest

from pypraticot5 import telefonista
from pypraticot5.telefone import Telefone


class TelefoneDeMentira(object):
    def __init__(self):
        self.numero = None

    def telefonar(self, numero):
        self.numero = numero
        return 'Telefonando de mentira para {}'.format(numero)


class TelefonistaBasicTests(unittest.TestCase):
    def test_instanciacao_telefonista(self):
        telefonista_obj = telefonista.Telefonista()
        self.assertListEqual([], telefonista_obj._contatos)
        self.assertIsInstance(telefonista_obj._telefone, Telefone)

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
        renzo = ('Renzo', '2345678')
        telefonista_obj = telefonista.Telefonista()
        telefonista_obj.adicionar(renzo)
        telefone_de_mentira = TelefoneDeMentira()
        ligacoes = list(telefonista_obj.ligar(telefone_de_mentira))
        self.assertListEqual(['Telefonando de mentira para 2345678. Olá Renzo'],
                             ligacoes)
        self.assertEqual(renzo[1], telefone_de_mentira.numero)

    def test_ligar_para_dois_contato(self):
        renzo = ('Renzo', '2345678')
        karen = ('Karen', '8765432')
        telefonista_obj = telefonista.Telefonista()
        telefonista_obj.adicionar(renzo)
        telefonista_obj.adicionar(karen)
        telefone_de_mentira = TelefoneDeMentira()
        ligacoes = list(telefonista_obj.ligar(telefone_de_mentira))
        self.assertListEqual(['Telefonando de mentira para 2345678. Olá Renzo',
                              'Telefonando de mentira para 8765432. Olá Karen'],
                             ligacoes)


class TelefonistaIntegracaoTests(unittest.TestCase):
    def test_ligar_para_dois_contato(self):
        renzo = ('Renzo', '2345678')
        telefonista_obj = telefonista.Telefonista()
        telefonista_obj.adicionar(renzo)
        ligacoes = list(telefonista_obj.ligar())
        self.assertListEqual(['Telefonando de verdade para 2345678. Olá Renzo'],
                             ligacoes)
