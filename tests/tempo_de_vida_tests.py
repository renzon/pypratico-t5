from datetime import datetime
from unittest.case import TestCase

from pypraticot5.tempo_de_vida import calcular_minutos


class MinutosDeVidaTests(TestCase):
    def test_recem_nascido(self):
        nascimento = datetime(2016, 5, 22, 11, 47, 0)
        minutos_de_vida = calcular_minutos(nascimento)
        self.assertEqual(1, minutos_de_vida)
