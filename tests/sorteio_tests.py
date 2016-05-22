from unittest.case import TestCase

from pypraticot5.sorteio import sortear, SorteioExcecao


class SortearTests(TestCase):
    def test_sortear_lista_unitaria(self):
        resultado = sortear([1])
        self.assertEqual(1, resultado)
        resultado = sortear([2])
        self.assertEqual(2, resultado)

    def test_sortear_lista_vazia(self):
        self.assertRaises(SorteioExcecao, sortear, [])

    def test_sortear_lista_com_10_elementos(self):
        resultado = sortear(list(range(2)))
        self.assertEqual(1, resultado)
