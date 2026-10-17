"""Validaciones reutilizables para el módulo de clientes (antes duplicadas)."""
import re

_PATRON_CORREO = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")


def es_correo_valido(correo: str) -> bool:
    """Devuelve True si el correo tiene un formato válido."""
    return bool(_PATRON_CORREO.match(correo or ""))
