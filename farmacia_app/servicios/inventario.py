from typing import List
from modelos.producto import Producto

class Inventario:
    """Clase para gestionar el inventario de productos."""
    def __init__(self):
        self.productos: List[Producto] = [] # encapsulacion

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def mostrar_productos(self) -> None:

        print("\nListado de productos del inventario:")
        print("-----------------------------")
        for p in self.productos:
            print(f"{p.nombre} - Precio Final: ${p.calcular_precio_final():.2f} - Stock: {p.get_stock()}")
            print("-----------------------------")