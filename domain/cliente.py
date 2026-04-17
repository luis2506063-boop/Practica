class Cliente:
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido

    def obtener_descuento(self, total:float) -> float:
        return 0.0 #El cliente normal no ahorra nada

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"


class ClienteVIP(Cliente):

    def obtener_descuento(self, total:float) -> float:
        #Aplicamos el 10% de descuento
        return total * 0.1

    def __str__(self):
        return f"Cliente VIP: {self.nombre} {self.apellido}"


class ClienteBlack(Cliente):

    def obtener_descuento(self, total:float) -> float:
        #El cliente Black ahorra un 30%
        return total * 0.3

    def __str__(self):
        return f"Cliente Black: {self.nombre} {self.apellido}"







