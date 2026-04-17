from domain.producto import Producto
from domain.cliente import Cliente, ClienteVIP, ClienteBlack
from domain.venta import Venta

# Datos iniciales
productos = [
    Producto(1, "Ramo 10 rosas",  250, 50),
    Producto(2, "Ramo 20 rosas",  450, 50),
    Producto(3, "Ramo tulipanes", 300, 100),
]

ventas = []
SEP = "-" * 40


# ──────────────────────────────────────────
# Helpers de visualización
# ──────────────────────────────────────────

def mostrar_productos():
    print(SEP)
    print("PRODUCTOS DISPONIBLES")
    print(SEP)
    for p in productos:
        print(p)
    print(SEP)


# ──────────────────────────────────────────
# Flujo: elegir cliente
# ──────────────────────────────────────────

def elegir_cliente() -> Cliente:
    print("\nTipo de cliente:")
    print("  1. Normal")
    print("  2. VIP    (10% descuento)")
    print("  3. Black  (30% descuento)")

    while True:
        opcion = input("Elige tipo [1-3]: ").strip()
        if opcion in ("1", "2", "3"):
            break
        print("Opción inválida, intenta de nuevo.")

    nombre  = input("Nombre:   ").strip()
    apellido = input("Apellido: ").strip()

    if opcion == "1":
        return Cliente(nombre, apellido)
    elif opcion == "2":
        return ClienteVIP(nombre, apellido)
    else:
        return ClienteBlack(nombre, apellido)


# ──────────────────────────────────────────
# Flujo: nueva venta
# ──────────────────────────────────────────

def nueva_venta():
    print(SEP)
    print("NUEVA VENTA")
    print(SEP)

    cliente = elegir_cliente()
    venta   = Venta(cliente)

    mostrar_productos()

    while True:
        entrada = input("ID del producto (o 'listo' para terminar): ").strip()

        if entrada.lower() == "listo":
            if not venta.productos:
                print("Agrega al menos un producto antes de terminar.")
                continue
            break

        # Validar que el ID sea numérico
        try:
            id_producto = int(entrada)
        except ValueError:
            print("El ID debe ser un número entero.")
            continue

        # Buscar el producto en la lista
        producto = next((p for p in productos if p.id == id_producto), None)
        if producto is None:
            print(f"No existe un producto con ID {id_producto}.")
            continue

        # Validar que la cantidad sea numérica
        try:
            cantidad = int(input(f"Cantidad de '{producto.nombre}': ").strip())
        except ValueError:
            print("La cantidad debe ser un número entero.")
            continue

        # Intentar agregar el producto (puede fallar por stock o cantidad <= 0)
        try:
            venta.agregar_producto(producto, cantidad)
            print(f"  Agregado: {producto.nombre} x{cantidad}")
        except ValueError as e:
            print(f"Error: {e}")

    print(SEP)
    print(venta)
    print(SEP)
    ventas.append(venta)
    print("Venta registrada exitosamente.")


# ──────────────────────────────────────────
# Flujo: historial de ventas
# ──────────────────────────────────────────

def ver_ventas():
    print(SEP)
    print("HISTORIAL DE VENTAS")
    print(SEP)
    if not ventas:
        print("No hay ventas registradas en esta sesión.")
    else:
        for i, v in enumerate(ventas, 1):
            print(f"Venta #{i}")
            print(v)
            print(SEP)


# ──────────────────────────────────────────
# Menú principal
# ──────────────────────────────────────────

def menu():
    while True:
        print("\n=== SISTEMA DE VENTAS ===")
        print("1. Ver productos")
        print("2. Nueva venta")
        print("3. Ver historial de ventas")
        print("0. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            nueva_venta()
        elif opcion == "3":
            ver_ventas()
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida, elige entre 0 y 3.")


if __name__ == "__main__":
    menu()
