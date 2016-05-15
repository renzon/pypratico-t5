import unittest

from pypraticot5 import telefone


class TelefoneTests(unittest.TestCase):
    def test_telefonar(self):
        telefone_obj = telefone.Telefone()
        resultado = telefone_obj.telefonar('2345678')
        self.assertEqual('Telefonando de verdade para 2345678', resultado)
        resultado = telefone_obj.telefonar('8765432')
        self.assertEqual('Telefonando de verdade para 8765432', resultado)
