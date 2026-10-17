def total_ventas(facturas: list) -> float:
    """Suma el total de una lista de facturas."""
    return sum(f["total"] for f in facturas)
