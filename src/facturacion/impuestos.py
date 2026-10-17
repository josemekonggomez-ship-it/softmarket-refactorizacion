IVA = 0.19


def aplicar_iva(subtotal: float) -> float:
    """Suma el IVA al subtotal y redondea a 2 decimales."""
    return round(subtotal * (1 + IVA), 2)
