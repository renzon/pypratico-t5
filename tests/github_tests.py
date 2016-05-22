from unittest.case import TestCase
from unittest.mock import Mock

from pypraticot5 import github
from pypraticot5.github import buscar_avatar


class BuscarAvatarBasicoUnitario(TestCase):
    def setUp(self):
        # Mockando Objetos
        response_mock = Mock()

        def json():
            return {'avatar_url': 'https://avatars.githubusercontent.com/u/3457115?v=3'}

        response_mock.json = json
        self.get_mock = Mock(return_value=response_mock)
        self.get_real = github.requests.get
        github.requests.get = self.get_mock

    def tearDown(self):
        # Desfazendo mock
        github.requests.get = self.get_real

    def test_buscar_avatar_de_usuario(self):
        # Realizando testes
        resultado = buscar_avatar('renzon')
        self.assertEqual('https://avatars.githubusercontent.com/u/3457115?v=3', resultado)
        self.get_mock.assert_called_once_with('https://api.github.com/users/renzon')




class BuscarAvatarIntegracao(TestCase):
    def test_buscar_avatar_de_usuario(self):
        resultado = buscar_avatar('rogerlista')
        self.assertEqual('https://avatars.githubusercontent.com/u/300170?v=3', resultado)
