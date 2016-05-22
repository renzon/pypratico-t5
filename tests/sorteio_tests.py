from unittest.case import TestCase
from unittest.mock import patch

from pypraticot5.sorteio import sortear, SorteioExcecao


class SortearTests(TestCase):
    def test_sortear_lista_unitaria(self):
        resultado = sortear([1])
        self.assertEqual(1, resultado)
        resultado = sortear([2])
        self.assertEqual(2, resultado)

    def test_sortear_lista_vazia(self):
        self.assertRaises(SorteioExcecao, sortear, [])

    @patch('pypraticot5.sorteio.choice')
    def test_sortear_lista_com_10_elementos(self, choice_mock):
        lista = list(range(2))
        choice_mock.return_value = lista[-1]
        resultado = sortear(lista)
        self.assertEqual(lista[-1], resultado)
        choice_mock.assert_called_once_with(lista)
