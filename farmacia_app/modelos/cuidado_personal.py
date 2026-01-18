from modelos.producto import Producto
# creacion de la clase CuidadoPersonal
# herencia + polimorfismo
class CuidadoPersonal(Producto):
    def __init__(self, nombre: str, precio: float, stock: int):
        super().__init__(nombre, precio, stock) # herencia

    def calcular_precio_final(self) -> float: # escritura polimorfismo
        return self.precio * 1.05  # impuesto menor