from domain.producto import Producto


class DetalleVenta:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self) -> float:
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad} = ${self.calcular_subtotal():.2f}"