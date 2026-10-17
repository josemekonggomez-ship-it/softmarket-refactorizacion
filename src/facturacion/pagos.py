"""Métodos de pago (patrón Strategy). Abierto a extensión, cerrado a modificación."""
from abc import ABC, abstractmethod


class MetodoPago(ABC):
    @abstractmethod
    def cobrar(self, monto: float) -> bool:
        """Intenta cobrar el monto y devuelve True si fue exitoso."""


class PagoTarjeta(MetodoPago):
    def cobrar(self, monto: float) -> bool:
        return monto > 0


class PagoPaypal(MetodoPago):
    def cobrar(self, monto: float) -> bool:
        return monto > 0
