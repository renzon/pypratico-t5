import unittest

from pypraticot5 import telefonista


class TelefonistasTests(unittest.TestCase):
    def test_instanciacao_telefonista(self):
        telefonista_obj = telefonista.Telefonista()
        self.assertListEqual([], telefonista_obj._contatos)

# telefonista_obj.adicionar(contato)
# contato = ('Renzo', '2345678')
