def validar_credenciales(usuario: str, clave: str) -> bool:
    """Rechaza credenciales vacías (corrección del error crítico en producción)."""
    return bool(usuario and clave)
