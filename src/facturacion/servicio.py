"""Servicio de facturación aplicando SOLID."""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from .pagos import MetodoPago


@dataclass
class Item:
    precio: float
    cantidad: int


class RepositorioFacturas(ABC):
    @abstractmethod
    def guardar(self, factura: dict) -> None: ...


class Notificador(ABC):
    @abstractmethod
    def notificar(self, destino: str, mensaje: str) -> None: ...


class CalculadoraTotal:
    def calcular(self, items: List[Item]) -> float:
        return sum(i.precio * i.cantidad for i in items)


class ServicioFacturacion:
    def __init__(self, calculadora: CalculadoraTotal,
                 repositorio: RepositorioFacturas,
                 notificador: Notificador):
        self.calculadora = calculadora
        self.repositorio = repositorio
        self.notificador = notificador

    def facturar(self, email_cliente: str, items: List[Item],
                 metodo_pago: MetodoPago) -> float:
        total = self.calculadora.calcular(items)
        if metodo_pago.cobrar(total):
            self.repositorio.guardar({"cliente": email_cliente, "total": total})
            self.notificador.notificar(email_cliente, "Su factura está lista")
        return total
