from domain.producto import Producto
from domain.cliente import Cliente
from domain.venta import Venta

productos = []
productos.append(Producto(1,"ramo 10 rosas", 250, 50))
productos.append(Producto(2,"ramo 20 rosas", 450, 50))
productos.append(Producto(3,"ramo tulipanes", 300, 100))

clientes = []
clientes.append(Cliente("Luis","Marin"))
clientes.append(Cliente("Carlos","Hernández"))

venta = Venta(clientes[0])  # 👈 AQUÍ defines el cliente

venta.agregar_producto(productos[0], 1)
venta.agregar_producto(productos[1], 2)

print(venta)


