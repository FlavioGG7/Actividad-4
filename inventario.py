inventario = {
    "P001": {"nombre": "Laptop", "precio": 12500.00, "stock": 8},
    "P002": {"nombre": "Mouse inalámbrico", "precio": 250.50, "stock": 40},
    "P003": {"nombre": "Teclado mecánico", "precio": 980.00, "stock": 3},
    "P004": {"nombre": "Monitor 24\"", "precio": 3200.00, "stock": 12},
    "P005": {"nombre": "Webcam HD", "precio": 650.75, "stock": 2},
    "P006": {"nombre": "Memoria USB 64GB", "precio": 120.00, "stock": 25},
}

STOCK_BAJO = 5


def valor_total(inventario):
    """Suma precio * stock de todos los productos."""
    return sum(p["precio"] * p["stock"] for p in inventario.values())


def producto_mas_caro(inventario):
    """Devuelve (codigo, datos) del producto con mayor precio."""
    return max(inventario.items(), key=lambda item: item[1]["precio"])


def producto_mas_barato(inventario):
    """Devuelve (codigo, datos) del producto con menor precio."""
    return min(inventario.items(), key=lambda item: item[1]["precio"])


def productos_stock_bajo(inventario, limite=STOCK_BAJO):
    """Devuelve un diccionario con los productos cuyo stock es menor al límite."""
    return {c: p for c, p in inventario.items() if p["stock"] < limite}


def listar_productos(inventario):
    print(f"{'Código':<8}{'Nombre':<20}{'Precio':>12}{'Stock':>8}{'Valor':>14}")
    print("-" * 62)
    for codigo, p in inventario.items():
        valor = p["precio"] * p["stock"]
        print(f"{codigo:<8}{p['nombre']:<20}${p['precio']:>10,.2f}{p['stock']:>8}  ${valor:>12,.2f}")


def main():
    if not inventario:
        print("El inventario está vacío.")
        return

    print("=" * 50)
    print("           REPORTE DE INVENTARIO")
    print("=" * 50)

    print()
    listar_productos(inventario)

    print(f"\nValor total del inventario: ${valor_total(inventario):,.2f}")

    codigo, p = producto_mas_caro(inventario)
    print(f"\nProducto más caro:   [{codigo}] {p['nombre']} - ${p['precio']:,.2f}")

    codigo, p = producto_mas_barato(inventario)
    print(f"Producto más barato: [{codigo}] {p['nombre']} - ${p['precio']:,.2f}")

    print(f"\nProductos con stock bajo (menos de {STOCK_BAJO} unidades):")
    bajos = productos_stock_bajo(inventario)
    if bajos:
        for codigo, p in bajos.items():
            print(f"  [{codigo}] {p['nombre']:<20} Stock: {p['stock']}")
    else:
        print("  Ninguno.")


if __name__ == "__main__":
    main()