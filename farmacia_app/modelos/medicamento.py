from modelos.producto import Producto
# creacion de la clase Medicamento 

# herencia + polimorfismo

class Medicamento(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, receta: bool):
        super().__init__(nombre, precio, stock) # herencia
        self.receta = receta

    def calcular_precio_final(self) -> float: # escritura polimorfismo
        return self.precio * 1.12  # impuesto