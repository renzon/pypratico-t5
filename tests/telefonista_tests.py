import unittest
from unittest.mock import Mock

from pypraticot5 import telefonista
from pypraticot5.telefone import Telefone


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
        telefone_de_mentira = Mock()
        telefone_de_mentira.telefonar = Mock(return_value='Telefonando de mentira para 2345678')
        telefonista_obj._telefone = telefone_de_mentira
        ligacoes = list(telefonista_obj.ligar())
        self.assertListEqual(['Telefonando de mentira para 2345678. Olá Renzo'],
                             ligacoes)
        telefone_de_mentira.telefonar.assert_called_once_with(renzo[1])

    def test_ligar_para_dois_contato(self):
        renzo = ('Renzo', '2345678')
        karen = ('Karen', '8765432')
        telefonista_obj = telefonista.Telefonista()
        telefonista_obj.adicionar(renzo)
        telefonista_obj.adicionar(karen)

        def side_effect(numero):
            return 'Telefonando de mentira para {}'.format(numero)

        telefone_de_mentira = Mock()
        telefone_de_mentira.telefonar = Mock(side_effect=side_effect)
        telefonista_obj._telefone = telefone_de_mentira
        ligacoes = list(telefonista_obj.ligar())
        self.assertListEqual(['Telefonando de mentira para 2345678. Olá Renzo',
                              'Telefonando de mentira para 8765432. Olá Karen'],
                             ligacoes)
        telefone_de_mentira.telefonar.assert_any_call('2345678')
        telefone_de_mentira.telefonar.assert_any_call('8765432')
        self.assertEqual(2, telefone_de_mentira.telefonar.call_count)


class TelefonistaIntegracaoTests(unittest.TestCase):
    def test_ligar_para_dois_contato(self):
        renzo = ('Renzo', '2345678')
        telefonista_obj = telefonista.Telefonista()
        telefonista_obj.adicionar(renzo)
        ligacoes = list(telefonista_obj.ligar())
        self.assertListEqual(['Telefonando de verdade para 2345678. Olá Renzo'],
                             ligacoes)
