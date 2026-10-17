import unittest
from src.facturacion.pagos import PagoTarjeta
from src.facturacion.servicio import (
    CalculadoraTotal, Item, Notificador, RepositorioFacturas, ServicioFacturacion)


class RepoFalso(RepositorioFacturas):
    def __init__(self):
        self.guardadas = []

    def guardar(self, factura):
        self.guardadas.append(factura)


class NotificadorFalso(Notificador):
    def __init__(self):
        self.enviados = []

    def notificar(self, destino, mensaje):
        self.enviados.append((destino, mensaje))


class TestFacturacion(unittest.TestCase):
    def test_facturar_guarda_y_notifica(self):
        repo, noti = RepoFalso(), NotificadorFalso()
        servicio = ServicioFacturacion(CalculadoraTotal(), repo, noti)
        total = servicio.facturar("ana@softmarket.com",
                                  [Item(10, 2), Item(5, 1)], PagoTarjeta())
        self.assertEqual(total, 25)
        self.assertEqual(len(repo.guardadas), 1)
        self.assertEqual(len(noti.enviados), 1)
