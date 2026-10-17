import unittest
from src.clientes.validaciones import es_correo_valido


class TestValidaciones(unittest.TestCase):
    def test_correo_valido(self):
        self.assertTrue(es_correo_valido("ana@softmarket.com"))

    def test_correo_invalido(self):
        self.assertFalse(es_correo_valido("ana@@softmarket"))
