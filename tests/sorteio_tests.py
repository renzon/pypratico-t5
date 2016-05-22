from unittest.case import TestCase

from pypraticot5.sorteio import sortear, SorteioExcecao


class SortearTests(TestCase):
    def test_sortear_lista_unitaria(self):
        resultado = sortear([1])
        self.assertEqual(1, resultado)
        resultado = sortear([2])
        self.assertEqual(2, resultado)

    def test_sortear_lista_vazia(self):
        try:
            sortear([])
        except SorteioExcecao:
            pass
        else:
            self.fail('Deveria ter lançado erro Sorteio Exceção')
