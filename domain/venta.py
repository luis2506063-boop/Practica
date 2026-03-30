# Hacemos una importación para registrar la fecha
from datetime import datetime

# Importamos las clases
from cliente import Cliente
from producto import Producto
from detalle_venta import DetalleVenta  # 🔥 nueva importación


class Venta:
    def __init__(self, cliente: Cliente) -> None:
        self.cliente = cliente
        self._productos = []  # lista de objetos DetalleVenta
        self.fecha = datetime.now()

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        # Validamos que la cantidad sea correcta
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")

        # Delegamos la lógica al producto (POO correcto)
        producto.vender(cantidad)

        # 🔥 Creamos un objeto DetalleVenta en lugar de diccionario
        detalle = DetalleVenta(producto, cantidad)

        self._productos.append(detalle)

    # Getter para proteger la lista
    @property
    def productos(self):
        return self._productos

    # -------------------------
    # CÁLCULOS
    # -------------------------

    def calcular_subtotal(self) -> float:
        subtotal = 0

        # 🔥 Ahora cada objeto sabe calcularse
        for detalle in self._productos:
            subtotal += detalle.calcular_subtotal()

        return subtotal

    def calcular_descuento(self) -> float:
        subtotal = self.calcular_subtotal()

        # 🔥 Polimorfismo (Cliente, VIP, Black)
        return self.cliente.obtener_descuento(subtotal)

    def calcular_total(self) -> float:
        subtotal = self.calcular_subtotal()
        descuento = self.calcular_descuento()

        return subtotal - descuento

    # -------------------------
    # REPRESENTACIÓN
    # -------------------------

    def __str__(self) -> str:
        lineas = []
        lineas.append(f"Cliente: {self.cliente}")
        lineas.append(f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}")
        lineas.append("Productos:")

        # 🔥 cada detalle se imprime solo
        for detalle in self._productos:
            lineas.append(f"- {detalle}")

        subtotal = self.calcular_subtotal()
        descuento = self.calcular_descuento()
        total = self.calcular_total()

        lineas.append(f"Subtotal: ${subtotal:.2f}")
        lineas.append(f"Descuento: ${descuento:.2f}")
        lineas.append(f"Total: ${total:.2f}")

        return "\n".join(lineas)