# Hacemos una importación para registrar la fecha
from datetime import datetime

# Importamos las clases
from cliente import Cliente
from producto import Producto


class Venta:
    def __init__(self, cliente: Cliente) -> None:
        self.cliente = cliente
        self._productos = []  # Encapsulamos la lista
        self.fecha = datetime.now()

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        # Validamos que la cantidad sea correcta
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")

        # Lógica de negocio (delegamos al producto)
        producto.vender(cantidad)

        # Creamos el detalle (composición)
        detalle = {
            'producto': producto,
            'cantidad': cantidad,
        }

        self._productos.append(detalle)

    # Getter para no exponer directamente la lista interna
    @property
    def productos(self):
        return self._productos

    # -------------------------
    # CÁLCULOS
    # -------------------------

    def calcular_subtotal(self) -> float:
        subtotal = 0

        for detalle in self._productos:
            producto = detalle['producto']
            cantidad = detalle['cantidad']

            # 🔴 CORRECCIÓN IMPORTANTE:
            # usamos el getter, NO el atributo protegido
            subtotal += producto.precio * cantidad

        return subtotal

    def calcular_descuento(self) -> float:
        subtotal = self.calcular_subtotal()

        # 🔥 AQUÍ USAMOS POLIMORFISMO
        # No importa si es Cliente, VIP o Black
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

        for detalle in self._productos:
            producto = detalle['producto']
            cantidad = detalle['cantidad']
            lineas.append(f"- {producto.nombre} x{cantidad} = ${producto.precio * cantidad}")

        subtotal = self.calcular_subtotal()
        descuento = self.calcular_descuento()
        total = self.calcular_total()

        lineas.append(f"Subtotal: ${subtotal:.2f}")
        lineas.append(f"Descuento: ${descuento:.2f}")
        lineas.append(f"Total: ${total:.2f}")

        return "\n".join(lineas)