from unittest.case import TestCase

from pypraticot5.sorteio import sortear


class SortearTests(TestCase):
    def test_sortear_lista_unitaria(self):
        resultado = sortear([1])
        self.assertEqual(1, resultado)
        resultado = sortear([2])
        self.assertEqual(2, resultado)
