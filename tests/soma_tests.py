import unittest

from pypraticot5 import soma


class SomaTests(unittest.TestCase):
    def testes_soma_de_zeros(self):
        resultado = soma.soma(0, 0)
        self.assertEqual(0, resultado)

    def testes_soma_de_positivos(self):
        resultado = soma.soma(2, 4)
        self.assertEqual(6, resultado)


if __name__ == '__main__':
    unittest.main()
