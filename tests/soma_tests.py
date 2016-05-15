import os
import sys
import unittest


diretorio_de_testes = os.path.dirname(__file__)
diretorio_do_projeto = os.path.join(diretorio_de_testes, '..')
diretorio_do_projeto = os.path.abspath(diretorio_do_projeto)
sys.path.append(diretorio_do_projeto)

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
