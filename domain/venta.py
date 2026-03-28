#Hacemos una importación para registrar la fecha
from datetime import datetime

#importamos las clases
from cliente import Cliente
from producto import Producto

class Venta:
    def __init__(self, cliente: Cliente) -> None:
        self.cliente = cliente
        self.productos = []
        self.fecha = datetime.now()

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        #validamos que la cantidad sea correcta
        if cantidad <= 0:
            raise ValueError("La cantidad no es mayor a 0")

        producto.vender(cantidad)

        detalle = {
            'producto': producto,
            'cantidad': cantidad,
            }

        self.productos.append(detalle)

    #Hacemos una función para calcular subtotal y total..
    def calcular_subtotal(self):
        subtotal = 0
        #Hacemos el ciclo for para obtener el objeto producto y la cantidad del diccionario
        for detalle in self.productos:
            producto = detalle['producto']
            cantidad = detalle['cantidad']
            #hacemos una operación para obtener el subtotal
            subtotal += producto._precio * cantidad


        return subtotal


