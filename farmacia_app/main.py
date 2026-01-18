from modelos.medicamento import Medicamento
from modelos.cuidado_personal import CuidadoPersonal
from servicios.inventario import Inventario

def main():
    inventario = Inventario()

    paracetamol = Medicamento("Paracetamol", 2.50, 50, True)
    jarabe = Medicamento("Jarabe", 4.00, 30, False)
    shampoo = CuidadoPersonal("Shampoo", 6.00, 20)

    inventario.agregar_producto(paracetamol)
    inventario.agregar_producto(jarabe)
    inventario.agregar_producto(shampoo)

    inventario.mostrar_productos()

if __name__ == "__main__":
    main()