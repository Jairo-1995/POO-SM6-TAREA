from abc import ABC, abstractmethod
# creacion de la clase Producto

# Clase base abstracta
class Producto(ABC):
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock # encapsulacion 

    def get_stock(self) -> int:
        return self.stock
    
    def actualizar_stock(self, cantidad: int) -> None:
        self.stock += cantidad

    @abstractmethod
    def calcular_precio_final(self) -> float:
        """"metodo de polimorfismo"""""
        pass