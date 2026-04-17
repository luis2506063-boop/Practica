class Producto:
    def __init__(self, id: int,nombre: str, precio: float, stock: int  ) -> None:
        self.id = id
        self.nombre = nombre
        #los siguientes atributos estarán privados con _ bajo
        self._precio = precio
        self._stock = stock

    #Encapsulamos ---
    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    #Vamos a protegernos para evitar errores de asignación mal de precios

    @precio.setter

    def precio(self, nuevo_precio: float) -> None:
        if nuevo_precio <= 0:
            raise ValueError("Precio debe ser mayor que 0")
        self._precio = nuevo_precio

    @stock.setter
    def stock(self, nuevo_stock: float) -> None:
        if nuevo_stock < 0:
            raise ValueError("Stock debe ser mayor que 0")
        self._stock = nuevo_stock


    #Métodos de negocio
    def vender(self, cantidad: int) -> None:
        #Evitamos solicitud negativa o solicitud de cero
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a 0")

        #No vender más de lo que hay
        if cantidad > self._stock:
            raise ValueError(f"Stock insuficiente para {self.nombre}. Disponible {self._stock}")
        self._stock -= cantidad

    def __str__(self):
        return f"ID: {self.id} | {self.nombre} | Precio: ${self._precio} | Stock: {self._stock}"
