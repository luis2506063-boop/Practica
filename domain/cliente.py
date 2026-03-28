class Cliente:
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido

    def obtener_descuento(self, total:float) -> float:
        return 0.0 #El cliente normal no ahorra nada


class ClienteVIP(Cliente):
    def __init__(self, nombre:str, apellido:str):
        super().__init__(nombre, apellido)

    def obtener_descuento(self, total:float) -> float:
        #Aplicamos el 10% de descuento
        descuento = total * 0.1
        return descuento


class ClienteBlack(Cliente):
    def __init__(self, nombre:str, apellido:str):
        super().__init__(nombre, apellido)

    def obtener_descuento(self, total:float) -> float:
        #Eñ cliente Black ahorra un 30%
        descuento = total * 0.3
        return descuento


