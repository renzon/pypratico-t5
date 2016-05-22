from datetime import datetime
from unittest.case import TestCase
from unittest.mock import patch

from pypraticot5.tempo_de_vida import calcular_minutos


class MinutosDeVidaTests(TestCase):
    @patch('pypraticot5.tempo_de_vida.agora')
    def test_recem_nascido(self, agora_mock):
        agora_mock.return_value = datetime(2016, 5, 22, 11, 48, 2)
        nascimento = datetime(2016, 5, 22, 11, 47, 0)
        minutos_de_vida = calcular_minutos(nascimento)
        self.assertEqual(1, minutos_de_vida)
