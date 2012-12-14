
from django.utils import unittest
from django.test.client import Client

class LoginTest(unittest.TestCase):
    def setUp(self):
        # Creamos el cliente
        self.client = Client()

    def test_details(self):
        # Emitimos una peticion POST
        response = self.client.post('/login/',{'username':'aquiponelusuario','password':'aquiponelpassword'})

        # Verificamos si la respuesta es 200
        self.assertEqual(response.context['error'], 'Su password o usuario es incorrecto')